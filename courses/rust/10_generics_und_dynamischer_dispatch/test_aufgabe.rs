// ============================================================================
// 🧪 TESTSUITE: RUST 10 GENERICS & DYNAMISCHER DISPATCH
// ============================================================================

#[allow(dead_code)]
#[path = "aufgabe.rs"]
mod aufgabe;

#[allow(unused_imports)]
use aufgabe::*;

// TEST: test_generic_data_container
#[test]
fn test_generic_data_container() {
    let container = DataContainer::new(42, "int-container");
    assert_eq!(*container.get_value(), 42);
    assert_eq!(container.tag, "int-container");

    let transformed = container.transform(|x| format!("Value is {}", x * 2));
    assert_eq!(*transformed.get_value(), "Value is 84");
    assert_eq!(transformed.tag, "int-container");
}

// TEST: test_individual_plugins
#[test]
fn test_individual_plugins() {
    let up = UppercasePlugin;
    assert_eq!(up.name(), "uppercase");
    assert_eq!(up.process("rust"), "RUST");

    let pre = PrefixPlugin { prefix: "LOG: ".to_string() };
    assert_eq!(pre.name(), "prefix");
    assert_eq!(pre.process("system ready"), "LOG: system ready");

    let censor = CensorPlugin {
        forbidden: "password123".to_string(),
        replacement: "********".to_string(),
    };
    assert_eq!(censor.name(), "censor");
    assert_eq!(censor.process("auth password123 ok"), "auth ******** ok");
}

// TEST: test_plugin_pipeline_dynamic_dispatch
#[test]
fn test_plugin_pipeline_dynamic_dispatch() {
    let mut pipeline = PluginPipeline::new();
    assert_eq!(pipeline.count(), 0);

    pipeline.register(Box::new(PrefixPlugin { prefix: "[AUDIT] ".to_string() }));
    pipeline.register(Box::new(UppercasePlugin));
    pipeline.register(Box::new(CensorPlugin {
        forbidden: "SECRET".to_string(),
        replacement: "XXX".to_string(),
    }));

    assert_eq!(pipeline.count(), 3);
    assert_eq!(pipeline.plugin_names(), vec!["prefix", "uppercase", "censor"]);

    let input = "user accessed secret token";
    let output = pipeline.execute(input);
    // 1. Prefix: "[AUDIT] user accessed secret token"
    // 2. Uppercase: "[AUDIT] USER ACCESSED SECRET TOKEN"
    // 3. Censor: "[AUDIT] USER ACCESSED XXX TOKEN"
    assert_eq!(output, "[AUDIT] USER ACCESSED XXX TOKEN");
}

fn main() {
    println!("🧪 Führe Rust 10 Testsuite aus...");
    test_generic_data_container();
    println!("  ✓ test_generic_data_container bestanden");
    test_individual_plugins();
    println!("  ✓ test_individual_plugins bestanden");
    test_plugin_pipeline_dynamic_dispatch();
    println!("  ✓ test_plugin_pipeline_dynamic_dispatch bestanden");
    println!("\n✅ Alle Tests für Rust 10 erfolgreich bestanden!");
}
