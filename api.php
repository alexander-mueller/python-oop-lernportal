<?php
/**
 * 🐘 GEHÄRTETES PHP REST API BACKEND FÜR SHARED-WEBSPACE (Hetzner, All-Inkl, Strato, cPanel)
 * =========================================================================================
 * - Signatur- und Ablauf-Prüfung für JWT-Tokens (Auth-Bypass behoben).
 * - Sicherer Secret-Key aus Umgebung / geschützter Datei.
 * - FastCGI Authorization Header Fallback.
 * - Anti-Cheat Obergrenze bei XP-Vergabe.
 * - Prepared Statements & SQL-Injection-Schutz.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: SAMEORIGIN');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

// 1. SECRET KEY LADEN
$secret_key = getenv('SECRET_KEY');
if (!$secret_key || strlen($secret_key) < 32) {
    $secret_file = __DIR__ . '/.secret_key';
    if (file_exists($secret_file)) {
        $secret_key = trim((string)file_get_contents($secret_file));
    } else {
        $secret_key = bin2hex(random_bytes(32));
        @file_put_contents($secret_file, $secret_key, LOCK_EX);
        @chmod($secret_file, 0600);
    }
}

// 2. DATENBANK VERBINDUNG
$db_file = __DIR__ . '/platform_data.db';
try {
    $pdo = new PDO('sqlite:' . $db_file);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Datenbankverbindung fehlgeschlagen']);
    exit;
}

// 3. TABELLEN INITIALISIERUNG
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

// 4. AUTH HELPER MIT SICHERER HMAC-VERIFIKATION
function get_auth_user(string $secret_key): ?array {
    $auth = '';
    if (isset($_SERVER['HTTP_AUTHORIZATION'])) {
        $auth = $_SERVER['HTTP_AUTHORIZATION'];
    } elseif (isset($_SERVER['REDIRECT_HTTP_AUTHORIZATION'])) {
        $auth = $_SERVER['REDIRECT_HTTP_AUTHORIZATION'];
    } elseif (function_exists('getallheaders')) {
        $headers = getallheaders();
        $auth = $headers['Authorization'] ?? $headers['authorization'] ?? '';
    }

    if (strpos($auth, 'Bearer ') === 0) {
        $token = substr($auth, 7);
        $parts = explode('.', $token);
        if (count($parts) === 2) {
            $payload_raw = base64_decode($parts[0], true);
            if ($payload_raw === false) return null;

            $expected_sig = hash_hmac('sha256', $parts[0], $secret_key);
            if (!hash_equals($expected_sig, $parts[1])) {
                return null; // Ungültige Signatur
            }

            $payload = json_decode($payload_raw, true);
            if ($payload && isset($payload['uid']) && isset($payload['exp'])) {
                if ($payload['exp'] < time()) {
                    return null; // Abgelaufen
                }
                return $payload;
            }
        }
    }
    return null;
}

function create_token(int $uid, string $email, string $role, string $secret_key): string {
    $payload_data = [
        'uid' => $uid,
        'email' => $email,
        'role' => $role,
        'exp' => time() + (86400 * 30)
    ];
    $payload = base64_encode((string)json_encode($payload_data));
    $sig = hash_hmac('sha256', $payload, $secret_key);
    return $payload . '.' . $sig;
}

$path = $_SERVER['PATH_INFO'] ?? $_GET['action'] ?? '';
$raw_input = file_get_contents('php://input');
$body = $raw_input ? (json_decode($raw_input, true) ?? []) : [];

// 1. REGISTER
if ($path === '/auth/register') {
    $email = strtolower(trim((string)($body['email'] ?? '')));
    $password = (string)($body['password'] ?? '');
    $name = trim((string)($body['name'] ?? ''));
    $role_input = $body['role'] ?? 'solo';
    $role = in_array($role_input, ['student', 'teacher', 'solo'], true) ? $role_input : 'solo';

    if (!filter_var($email, FILTER_VALIDATE_EMAIL) || strlen($password) < 6 || strlen($name) < 1) {
        http_response_code(400);
        echo json_encode(['error' => 'Ungültige Eingabedaten']);
        exit;
    }

    $salt = bin2hex(random_bytes(16));
    $hash = hash_pbkdf2('sha256', $password, $salt, 100000);

    try {
        $stmt = $pdo->prepare("INSERT INTO users (email, password_hash, salt, name, role) VALUES (?, ?, ?, ?, ?)");
        $stmt->execute([$email, $hash, $salt, $name, $role]);
        $uid = (int)$pdo->lastInsertId();
        $token = create_token($uid, $email, $role, $secret_key);
        http_response_code(201);
        echo json_encode(['token' => $token, 'user' => ['id' => $uid, 'email' => $email, 'name' => $name, 'role' => $role, 'xp' => 0, 'level' => 1]]);
    } catch (PDOException $e) {
        http_response_code(409);
        echo json_encode(['error' => 'E-Mail existiert bereits']);
    }
    exit;
}

// 2. LOGIN (mit Constant-Time Dummy PBKDF2)
if ($path === '/auth/login') {
    $email = strtolower(trim((string)($body['email'] ?? '')));
    $password = (string)($body['password'] ?? '');

    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user) {
        $hash = hash_pbkdf2('sha256', $password, $user['salt'], 100000);
        if (hash_equals($hash, $user['password_hash'])) {
            $token = create_token((int)$user['id'], $user['email'], $user['role'], $secret_key);
            echo json_encode([
                'token' => $token,
                'user' => [
                    'id' => (int)$user['id'],
                    'email' => $user['email'],
                    'name' => $user['name'],
                    'role' => $user['role'],
                    'xp' => (int)$user['xp'],
                    'level' => (int)$user['level']
                ]
            ]);
            exit;
        }
    } else {
        hash_pbkdf2('sha256', $password, 'dummy_salt_fixed', 100000);
    }

    http_response_code(401);
    echo json_encode(['error' => 'Ungültige Anmeldedaten']);
    exit;
}

// 3. PROGRESS SAVE
if ($path === '/progress/save') {
    $user = get_auth_user($secret_key);
    if (!$user) { http_response_code(401); echo json_encode(['error' => 'Nicht angemeldet']); exit; }

    $chapter_id = substr(trim((string)($body['chapter_id'] ?? '')), 0, 120);
    $code_draft = substr((string)($body['code_draft'] ?? ''), 0, 100000);

    $stmt = $pdo->prepare("INSERT INTO chapter_progress (user_id, chapter_id, code_draft) VALUES (?, ?, ?) ON CONFLICT(user_id, chapter_id) DO UPDATE SET code_draft = excluded.code_draft, updated_at = CURRENT_TIMESTAMP");
    $stmt->execute([$user['uid'], $chapter_id, $code_draft]);
    echo json_encode(['status' => 'saved']);
    exit;
}

// 4. PROGRESS SOLVE (mit Anti-Cheat Cap)
if ($path === '/progress/solve') {
    $user = get_auth_user($secret_key);
    if (!$user) { http_response_code(401); echo json_encode(['error' => 'Nicht angemeldet']); exit; }

    $chapter_id = substr(trim((string)($body['chapter_id'] ?? '')), 0, 120);
    $xp_reward = min(max(0, (int)($body['xp_reward'] ?? 100)), 100);

    $stmt = $pdo->prepare("INSERT INTO chapter_progress (user_id, chapter_id, is_solved, solved_at) VALUES (?, ?, 1, CURRENT_TIMESTAMP) ON CONFLICT(user_id, chapter_id) DO UPDATE SET is_solved = 1, solved_at = CURRENT_TIMESTAMP");
    $stmt->execute([$user['uid'], $chapter_id]);

    $stmt = $pdo->prepare("UPDATE users SET xp = xp + ?, level = ((xp + ?) / 100) + 1 WHERE id = ?");
    $stmt->execute([$xp_reward, $xp_reward, $user['uid']]);

    echo json_encode(['status' => 'solved', 'earned_xp' => $xp_reward]);
    exit;
}

http_response_code(404);
echo json_encode(['error' => 'Endpunkt nicht gefunden']);
