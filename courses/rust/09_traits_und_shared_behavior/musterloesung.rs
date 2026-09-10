// ============================================================================
// 🦀 RUST 09: TRAITS & SHARED BEHAVIOR (MUSTERLÖSUNG)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
pub struct CpuMetric {
    pub core_id: usize,
    pub usage_percent: f64,
}

#[derive(Debug, Clone, PartialEq)]
pub struct DiskAlert {
    pub device: String,
    pub free_space_gb: u32,
    pub critical_override: Option<bool>,
}

pub trait TelemetryReport {
    fn summary(&self) -> String;

    fn severity_level(&self) -> u8 {
        1
    }

    fn is_critical(&self) -> bool {
        self.severity_level() >= 8
    }
}

pub trait FormatJson {
    fn to_json(&self) -> String;
}

impl TelemetryReport for CpuMetric {
    fn summary(&self) -> String {
        format!("CPU[{}]: {:.1}%", self.core_id, self.usage_percent)
    }

    fn severity_level(&self) -> u8 {
        if self.usage_percent >= 90.0 {
            9
        } else if self.usage_percent >= 75.0 {
            5
        } else {
            1
        }
    }
}

impl FormatJson for CpuMetric {
    fn to_json(&self) -> String {
        format!(
            r#"{{"type":"cpu","core_id":{},"usage_percent":{:.1}}}"#,
            self.core_id, self.usage_percent
        )
    }
}

impl TelemetryReport for DiskAlert {
    fn summary(&self) -> String {
        format!("Disk[{}]: {} GB free", self.device, self.free_space_gb)
    }

    fn severity_level(&self) -> u8 {
        if self.free_space_gb < 5 {
            10
        } else if self.free_space_gb < 20 {
            6
        } else {
            2
        }
    }

    fn is_critical(&self) -> bool {
        if let Some(c) = self.critical_override {
            c
        } else {
            self.severity_level() >= 8
        }
    }
}

impl FormatJson for DiskAlert {
    fn to_json(&self) -> String {
        format!(
            r#"{{"type":"disk","device":"{}","free_space_gb":{}}}"#,
            self.device, self.free_space_gb
        )
    }
}

pub fn format_and_dispatch<T: TelemetryReport + FormatJson>(item: &T) -> String {
    format!("[SEV {}] JSON: {}", item.severity_level(), item.to_json())
}

pub fn filter_critical<'a, T: TelemetryReport>(items: &'a [T]) -> Vec<&'a T> {
    items.iter().filter(|item| item.is_critical()).collect()
}

pub fn create_default_reporter() -> impl TelemetryReport {
    CpuMetric {
        core_id: 0,
        usage_percent: 0.0,
    }
}

fn main() {
    println!("=== Rust 09: Traits & Shared Behavior ===");
    let cpu = CpuMetric {
        core_id: 0,
        usage_percent: 94.5,
    };
    let disk = DiskAlert {
        device: "/dev/sda1".to_string(),
        free_space_gb: 3,
        critical_override: None,
    };

    println!("CPU: {}", cpu.summary());
    println!("Disk: {}", disk.summary());
    println!("CPU Dispatch: {}", format_and_dispatch(&cpu));

    let items = vec![
        cpu.clone(),
        CpuMetric {
            core_id: 1,
            usage_percent: 45.0,
        },
    ];
    let critical = filter_critical(&items);
    println!("Kritische CPU-Metriken: {}", critical.len());
}
