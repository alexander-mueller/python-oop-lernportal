// ============================================================================
// 🧪 TESTSUITE: RUST 09 TRAITS & SHARED BEHAVIOR
// ============================================================================

#[allow(dead_code)]
#[path = "aufgabe.rs"]
mod aufgabe;

#[allow(unused_imports)]
use aufgabe::*;

// TEST: test_cpu_metric_telemetry
#[test]
fn test_cpu_metric_telemetry() {
    let cpu_normal = CpuMetric { core_id: 0, usage_percent: 42.0 };
    assert_eq!(cpu_normal.summary(), "CPU[0]: 42.0%");
    assert_eq!(cpu_normal.severity_level(), 1);
    assert_eq!(cpu_normal.is_critical(), false);

    let cpu_high = CpuMetric { core_id: 1, usage_percent: 78.5 };
    assert_eq!(cpu_high.severity_level(), 5);
    assert_eq!(cpu_high.is_critical(), false);

    let cpu_crit = CpuMetric { core_id: 2, usage_percent: 95.0 };
    assert_eq!(cpu_crit.severity_level(), 9);
    assert_eq!(cpu_crit.is_critical(), true);
}

// TEST: test_disk_alert_telemetry
#[test]
fn test_disk_alert_telemetry() {
    let disk_ok = DiskAlert { device: "/dev/sda1".to_string(), free_space_gb: 50, critical_override: None };
    assert_eq!(disk_ok.summary(), "Disk[/dev/sda1]: 50 GB free");
    assert_eq!(disk_ok.severity_level(), 2);
    assert_eq!(disk_ok.is_critical(), false);

    let disk_warn = DiskAlert { device: "/dev/sdb1".to_string(), free_space_gb: 15, critical_override: None };
    assert_eq!(disk_warn.severity_level(), 6);
    assert_eq!(disk_warn.is_critical(), false);

    let disk_crit = DiskAlert { device: "/dev/nvme0n1".to_string(), free_space_gb: 2, critical_override: None };
    assert_eq!(disk_crit.severity_level(), 10);
    assert_eq!(disk_crit.is_critical(), true);

    let disk_forced_crit = DiskAlert { device: "/dev/sdc".to_string(), free_space_gb: 100, critical_override: Some(true) };
    assert_eq!(disk_forced_crit.is_critical(), true);
}

// TEST: test_format_json_and_dispatch
#[test]
fn test_format_json_and_dispatch() {
    let cpu = CpuMetric { core_id: 3, usage_percent: 91.0 };
    let json_str = cpu.to_json();
    assert!(json_str.contains(r#""type":"cpu""#));
    assert!(json_str.contains(r#""core_id":3"#));

    let dispatch_output = format_and_dispatch(&cpu);
    assert_eq!(dispatch_output, format!("[SEV 9] JSON: {}", json_str));
}

// TEST: test_filter_critical_and_default_reporter
#[test]
fn test_filter_critical_and_default_reporter() {
    let list = vec![
        CpuMetric { core_id: 0, usage_percent: 10.0 },
        CpuMetric { core_id: 1, usage_percent: 98.0 },
        CpuMetric { core_id: 2, usage_percent: 91.5 },
    ];
    let criticals = filter_critical(&list);
    assert_eq!(criticals.len(), 2);
    assert_eq!(criticals[0].core_id, 1);
    assert_eq!(criticals[1].core_id, 2);

    let default_rep = create_default_reporter();
    assert_eq!(default_rep.summary(), "CPU[0]: 0.0%");
    assert_eq!(default_rep.severity_level(), 1);
    assert_eq!(default_rep.is_critical(), false);
}

fn main() {
    println!("🧪 Führe Rust 09 Testsuite aus...");
    test_cpu_metric_telemetry();
    println!("  ✓ test_cpu_metric_telemetry bestanden");
    test_disk_alert_telemetry();
    println!("  ✓ test_disk_alert_telemetry bestanden");
    test_format_json_and_dispatch();
    println!("  ✓ test_format_json_and_dispatch bestanden");
    test_filter_critical_and_default_reporter();
    println!("  ✓ test_filter_critical_and_default_reporter bestanden");
    println!("\n✅ Alle Tests für Rust 09 erfolgreich bestanden!");
}
