// 🦀 Rust 01: Musterlösung
// =========================

pub fn create_system_specs() -> (String, u32, f64, bool) {
    let os = "Linux".to_string();
    let ram_mb: u32 = 16384;
    let cpu_ghz: f64 = 3.8;
    let is_64bit: bool = true;
    (os, ram_mb, cpu_ghz, is_64bit)
}

pub fn calculate_average_load(cores: u32, total_ticks: u64) -> f64 {
    if cores == 0 {
        return 0.0;
    }
    (total_ticks as f64) / (cores as f64)
}

pub fn format_sensor_reading(sensor_id: u16, temp_celsius: f32, is_alert: bool) -> String {
    let status = if is_alert { "ALERT" } else { "NORMAL" };
    format!("Sensor #{}: {}°C {}", sensor_id, temp_celsius, status)
}

pub fn demonstrate_shadowing_and_arrays(input_str: &str) -> [i32; 4] {
    let val: i32 = input_str.trim().parse().unwrap_or(0);
    [val, val * 2, val * 3, val * 4]
}

pub fn calculate_disk_utilization_percent(used_bytes: u64, total_bytes: u64) -> f64 {
    if total_bytes == 0 {
        return 0.0;
    }
    if used_bytes >= total_bytes {
        return 100.0;
    }
    ((used_bytes as f64) / (total_bytes as f64)) * 100.0
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
