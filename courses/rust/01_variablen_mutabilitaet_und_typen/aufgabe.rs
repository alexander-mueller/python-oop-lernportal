// 🦀 Rust 01: Variablen, Mutabilität & Typensystem
// ===============================================

// 🎯 TEILZIEL 1 (TODO 1): Gib ein System-Spezifikations-Tupel zurück
// Typ: (OS-Name: String, RAM_MB: u32, CPU_GHz: f64, Is_64Bit: bool)
// Erwartete Werte: ("Linux".to_string(), 16384, 3.8, true)
pub fn create_system_specs() -> (String, u32, f64, bool) {
    // TODO: Erstelle das Tupel und gib es zurück
    (String::new(), 0, 0.0, false)
}

// 🎯 TEILZIEL 2 (TODO 2): Berechne die durchschnittliche CPU-Last pro Kern
// Formel: total_ticks / cores als f64
// Falls cores == 0 ist, gib 0.0 zurück.
// Nutze explizites Casting mit `as f64`!
pub fn calculate_average_load(cores: u32, total_ticks: u64) -> f64 {
    // TODO: Prüfe auf cores == 0 und führe die Typkonvertierung mit `as f64` durch
    0.0
}

// 🎯 TEILZIEL 3 (TODO 3): Formatiere eine Sensor-Messung mit `format!()`
// Format: "Sensor #[id]: [temp]°C [STATUS]"
// Wenn is_alert == true ist, lautet STATUS "ALERT", sonst "NORMAL".
// Beispiel: format_sensor_reading(101, 42.5, true) -> "Sensor #101: 42.5°C ALERT"
// Beispiel: format_sensor_reading(4, 21.0, false)   -> "Sensor #4: 21°C NORMAL" bzw. "Sensor #4: 21.0°C NORMAL" (je nach float)
pub fn format_sensor_reading(sensor_id: u16, temp_celsius: f32, is_alert: bool) -> String {
    // TODO: Verwende format!() und prüfe is_alert
    String::new()
}

// 🎯 TEILZIEL 4 (TODO 4): Demonstriere Shadowing und erstelle ein Array fester Größe [i32; 4]
// 1. Nimm input_str (z. B. "10"), parse ihn via `.parse::<i32>().unwrap_or(0)` in dieselbe Variable (Shadowing).
// 2. Erstelle und gib ein 4-elementiges Array zurück mit: [val, val * 2, val * 3, val * 4]
pub fn demonstrate_shadowing_and_arrays(input_str: &str) -> [i32; 4] {
    // TODO: Wende Shadowing an und gib das Array [i32; 4] zurück
    [0, 0, 0, 0]
}

// 🎯 TEILZIEL 5 (TODO 5): Berechne die prozentuale Festplattenbelegung
// Formel: (used_bytes / total_bytes) * 100.0
// Randfälle:
// - total_bytes == 0 -> 0.0
// - used_bytes >= total_bytes -> 100.0
pub fn calculate_disk_utilization_percent(used_bytes: u64, total_bytes: u64) -> f64 {
    // TODO: Behandle Randfälle und berechne den Prozentwert als f64
    0.0
}

fn main() {
    let (os, ram, cpu, is_64) = create_system_specs();
    println!("System: {} mit {} MB RAM @ {:.1} GHz (64-Bit: {})", os, ram, cpu, is_64);

    let avg = calculate_average_load(8, 24000);
    println!("Durchschnittslast pro Kern: {:.2} Ticks", avg);

    println!("{}", format_sensor_reading(101, 42.5, true));
    println!("Array: {:?}", demonstrate_shadowing_and_arrays("12"));
    println!("Festplatte: {:.2}%", calculate_disk_utilization_percent(250, 1000));
}
