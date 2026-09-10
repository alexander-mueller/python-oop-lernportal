// ============================================================================
// 🦀 RUST 09: TRAITS & SHARED BEHAVIOR
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

// 🎯 TODO 1: Definiere den Trait 'TelemetryReport'
// Methoden:
// - fn summary(&self) -> String;
// - fn severity_level(&self) -> u8 (Default: liefert 1)
// - fn is_critical(&self) -> bool (Default: liefert true, wenn self.severity_level() >= 8)
pub trait TelemetryReport {
    // TODO: Methoden und Default-Implementierungen deklarieren
}

// 🎯 TODO 2: Definiere den Trait 'FormatJson'
// Methode:
// - fn to_json(&self) -> String;
pub trait FormatJson {
    // TODO: Methode deklarieren
}

// 🎯 TODO 3: Implementiere 'TelemetryReport' und 'FormatJson' für 'CpuMetric' und 'DiskAlert'
// Für CpuMetric:
// - summary: format!("CPU[{}]: {:.1}%", self.core_id, self.usage_percent)
// - severity_level: 9 wenn usage >= 90.0, 5 wenn usage >= 75.0, sonst 1
// - to_json: format!(r#"{{"type":"cpu","core_id":{},"usage_percent":{:.1}}}"#, self.core_id, self.usage_percent)
//
// Für DiskAlert:
// - summary: format!("Disk[{}]: {} GB free", self.device, self.free_space_gb)
// - severity_level: 10 wenn free_space < 5, 6 wenn free_space < 20, sonst 2
// - is_critical: wenn critical_override Some(b) ist, gib b zurück; sonst default (severity >= 8)
// - to_json: format!(r#"{{"type":"disk","device":"{}","free_space_gb":{}}}"#, self.device, self.free_space_gb)

// TODO: impl TelemetryReport for CpuMetric ...
// TODO: impl FormatJson for CpuMetric ...
// TODO: impl TelemetryReport for DiskAlert ...
// TODO: impl FormatJson for DiskAlert ...

// 🎯 TODO 4: Implementiere 'format_and_dispatch' mit Trait Bounds
// Signatur: fn format_and_dispatch<T: TelemetryReport + FormatJson>(item: &T) -> String
// Format: format!("[SEV {}] JSON: {}", item.severity_level(), item.to_json())
pub fn format_and_dispatch<T>(item: &T) -> String {
    // TODO: Trait Bounds deklarieren und String formatieren
    String::new()
}

// 🎯 TODO 5: Implementiere 'filter_critical'
// Filtert einen Slice von Items und liefert Referenzen auf alle kritischen Reports.
pub fn filter_critical<'a, T: TelemetryReport>(items: &'a [T]) -> Vec<&'a T> {
    // TODO: Mit .iter() und .filter() nach is_critical() filtern
    Vec::new()
}

// 🎯 TODO 6: Implementiere 'create_default_reporter' mit 'impl Trait' Rückgabetyp
// Liefert eine Standard-CpuMetric mit core_id 0 und usage_percent 0.0
pub fn create_default_reporter() -> impl TelemetryReport {
    // TODO: CpuMetric instanziieren und zurückgeben
    CpuMetric { core_id: 0, usage_percent: 0.0 }
}

fn main() {
    println!("=== Rust 09: Traits & Shared Behavior ===");
    let cpu = CpuMetric { core_id: 0, usage_percent: 94.5 };
    let disk = DiskAlert { device: "/dev/sda1".to_string(), free_space_gb: 3, critical_override: None };

    println!("CPU: {}", cpu.summary());
    println!("Disk: {}", disk.summary());
    println!("CPU Dispatch: {}", format_and_dispatch(&cpu));
}
