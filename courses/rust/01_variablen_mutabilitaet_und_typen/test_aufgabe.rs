// 🦀 Testsuite für Rust 01: Variablen, Mutabilität & Typensystem

#[test]
fn test_create_system_specs() {
    let (os, ram, cpu, is_64) = create_system_specs();
    assert_eq!(os, "Linux");
    assert_eq!(ram, 16384);
    assert!((cpu - 3.8).abs() < 0.001, "CPU Takt sollte 3.8 sein");
    assert!(is_64, "is_64bit sollte true sein");
}

#[test]
fn test_calculate_average_load() {
    let load = calculate_average_load(8, 24000);
    assert!((load - 3000.0).abs() < 0.001);

    let zero_cores = calculate_average_load(0, 1000);
    assert_eq!(zero_cores, 0.0);

    let partial = calculate_average_load(4, 10);
    assert!((partial - 2.5).abs() < 0.001);
}

#[test]
fn test_format_sensor_reading() {
    let alert_msg = format_sensor_reading(101, 42.5, true);
    assert_eq!(alert_msg, "Sensor #101: 42.5°C ALERT");

    let normal_msg = format_sensor_reading(5, 19.0, false);
    assert!(normal_msg.starts_with("Sensor #5:"));
    assert!(normal_msg.ends_with("NORMAL"));
}

#[test]
fn test_demonstrate_shadowing_and_arrays() {
    let arr = demonstrate_shadowing_and_arrays("10");
    assert_eq!(arr, [10, 20, 30, 40]);

    let arr2 = demonstrate_shadowing_and_arrays("  7  ");
    assert_eq!(arr2, [7, 14, 21, 28]);

    let fallback = demonstrate_shadowing_and_arrays("invalid");
    assert_eq!(fallback, [0, 0, 0, 0]);
}

#[test]
fn test_calculate_disk_utilization_percent() {
    let p1 = calculate_disk_utilization_percent(250, 1000);
    assert!((p1 - 25.0).abs() < 0.001);

    let p_full = calculate_disk_utilization_percent(1000, 1000);
    assert_eq!(p_full, 100.0);

    let p_over = calculate_disk_utilization_percent(1200, 1000);
    assert_eq!(p_over, 100.0);

    let p_zero = calculate_disk_utilization_percent(500, 0);
    assert_eq!(p_zero, 0.0);
}
