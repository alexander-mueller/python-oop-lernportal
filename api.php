<?php
/**
 * 🐘 PHP BACKEND REST API FÜR STANDARD-WEBSPACE (Hetzner, All-Inkl, Strato, cPanel)
 * ==============================================================================
 * SQLite-basierte REST-API für Benutzerverwaltung, Cloud-Speichern & Lehrerklassen.
 */

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

$db_file = __DIR__ . '/platform_data.db';
$pdo = new PDO('sqlite:' . $db_file);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Init Tabellen
$pdo->exec("
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    name TEXT NOT NULL,
    role TEXT DEFAULT 'student',
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    streak_days INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS chapter_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    chapter_id TEXT NOT NULL,
    code_draft TEXT,
    subgoals_json TEXT,
    is_solved INTEGER DEFAULT 0,
    solved_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, chapter_id)
);
CREATE TABLE IF NOT EXISTS classrooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    invite_code TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS class_enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    classroom_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(classroom_id, user_id)
);
");

$path = $_SERVER['PATH_INFO'] ?? $_GET['action'] ?? '';
$body = json_decode(file_get_contents('php://input'), true) ?? [];

// Helper Auth
function get_auth_user($pdo) {
    $headers = getallheaders();
    $auth = $headers['Authorization'] ?? $headers['authorization'] ?? '';
    if (strpos($auth, 'Bearer ') === 0) {
        $token = substr($auth, 7);
        $parts = explode('.', $token);
        if (count($parts) === 2) {
            $payload = json_decode(base64_decode($parts[0]), true);
            if ($payload && isset($payload['uid'])) {
                return $payload;
            }
        }
    }
    return null;
}

function create_token($uid, $email, $role) {
    $payload = base64_encode(json_encode(['uid' => $uid, 'email' => $email, 'role' => $role]));
    $sig = hash_hmac('sha256', $payload, 'python_lernportal_secret');
    return $payload . '.' . $sig;
}

// 1. REGISTER
if ($path === '/auth/register') {
    $email = strtolower(trim($body['email'] ?? ''));
    $password = $body['password'] ?? '';
    $name = trim($body['name'] ?? '');
    $role = $body['role'] ?? 'student';

    if (!$email || !$password || !$name) {
        http_response_code(400);
        echo json_encode(['error' => 'Pflichtfelder fehlen']);
        exit;
    }

    $salt = bin2hex(random_bytes(16));
    $hash = hash_pbkdf2('sha256', $password, $salt, 100000);

    try {
        $stmt = $pdo->prepare("INSERT INTO users (email, password_hash, salt, name, role) VALUES (?, ?, ?, ?, ?)");
        $stmt->execute([$email, $hash, $salt, $name, $role]);
        $uid = $pdo->lastInsertId();
        $token = create_token($uid, $email, $role);
        http_response_code(201);
        echo json_encode(['token' => $token, 'user' => ['id' => $uid, 'email' => $email, 'name' => $name, 'role' => $role, 'xp' => 0, 'level' => 1]]);
    } catch (Exception $e) {
        http_response_code(409);
        echo json_encode(['error' => 'E-Mail existiert bereits']);
    }
    exit;
}

// 2. LOGIN
if ($path === '/auth/login') {
    $email = strtolower(trim($body['email'] ?? ''));
    $password = $body['password'] ?? '';

    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user) {
        $hash = hash_pbkdf2('sha256', $password, $user['salt'], 100000);
        if (hash_equals($hash, $user['password_hash'])) {
            $token = create_token($user['id'], $user['email'], $user['role']);
            echo json_encode([
                'token' => $token,
                'user' => [
                    'id' => $user['id'],
                    'email' => $user['email'],
                    'name' => $user['name'],
                    'role' => $user['role'],
                    'xp' => (int)$user['xp'],
                    'level' => (int)$user['level']
                ]
            ]);
            exit;
        }
    }
    http_response_code(401);
    echo json_encode(['error' => 'Ungültige Anmeldedaten']);
    exit;
}

// 3. PROGRESS SAVE
if ($path === '/progress/save') {
    $user = get_auth_user($pdo);
    if (!$user) { http_response_code(401); echo json_encode(['error' => 'Nicht angemeldet']); exit; }

    $chapter_id = $body['chapter_id'] ?? '';
    $code_draft = $body['code_draft'] ?? '';

    $stmt = $pdo->prepare("INSERT INTO chapter_progress (user_id, chapter_id, code_draft) VALUES (?, ?, ?) ON CONFLICT(user_id, chapter_id) DO UPDATE SET code_draft = excluded.code_draft, updated_at = CURRENT_TIMESTAMP");
    $stmt->execute([$user['uid'], $chapter_id, $code_draft]);
    echo json_encode(['status' => 'saved']);
    exit;
}

// 4. PROGRESS SOLVE
if ($path === '/progress/solve') {
    $user = get_auth_user($pdo);
    if (!$user) { http_response_code(401); echo json_encode(['error' => 'Nicht angemeldet']); exit; }

    $chapter_id = $body['chapter_id'] ?? '';
    $xp_reward = (int)($body['xp_reward'] ?? 100);

    $stmt = $pdo->prepare("INSERT INTO chapter_progress (user_id, chapter_id, is_solved, solved_at) VALUES (?, ?, 1, CURRENT_TIMESTAMP) ON CONFLICT(user_id, chapter_id) DO UPDATE SET is_solved = 1, solved_at = CURRENT_TIMESTAMP");
    $stmt->execute([$user['uid'], $chapter_id]);

    $stmt = $pdo->prepare("UPDATE users SET xp = xp + ?, level = ((xp + ?) / 100) + 1 WHERE id = ?");
    $stmt->execute([$xp_reward, $xp_reward, $user['uid']]);

    echo json_encode(['status' => 'solved', 'earned_xp' => $xp_reward]);
    exit;
}

http_response_code(404);
echo json_encode(['error' => 'Endpunkt nicht gefunden']);
