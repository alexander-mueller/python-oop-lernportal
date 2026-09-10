// ============================================================================
// 🦀 RUST 10: GENERICS & DYNAMISCHER DISPATCH (TRAIT OBJECTS)
// ============================================================================

// 🎯 TODO 1: Implementiere das generische Struct 'DataContainer<T>'
// Felder:
// - pub value: T
// - pub tag: String
//
// Methoden:
// - pub fn new(value: T, tag: &str) -> Self
// - pub fn get_value(&self) -> &T
// - pub fn transform<U, F: FnOnce(T) -> U>(self, op: F) -> DataContainer<U>
#[derive(Debug, Clone, PartialEq)]
pub struct DataContainer<T> {
    pub value: T,
    pub tag: String,
}

impl<T> DataContainer<T> {
    // TODO: new und get_value implementieren
    pub fn new(value: T, tag: &str) -> Self {
        Self {
            value,
            tag: tag.to_string(),
        }
    }

    pub fn get_value(&self) -> &T {
        &self.value
    }

    pub fn transform<U, F: FnOnce(T) -> U>(self, op: F) -> DataContainer<U> {
        // TODO: op(self.value) anwenden und neuen DataContainer mit unverändertem tag erzeugen
        let new_val = op(self.value);
        DataContainer {
            value: new_val,
            tag: self.tag,
        }
    }
}

// 🎯 TODO 2: Definiere den Trait 'DataPlugin'
// Methoden:
// - fn name(&self) -> &str;
// - fn process(&self, input: &str) -> String;
pub trait DataPlugin {
    // TODO: Methodensignaturen deklarieren
}

// 🎯 TODO 3: Implementiere konkrete Plugins
// a) 'UppercasePlugin' -> name: "uppercase", process: input.to_uppercase()
pub struct UppercasePlugin;

// b) 'PrefixPlugin' -> Felder: pub prefix: String
//    name: "prefix", process: format!("{}{}", self.prefix, input)
pub struct PrefixPlugin {
    pub prefix: String,
}

// c) 'CensorPlugin' -> Felder: pub forbidden: String, pub replacement: String
//    name: "censor", process: input.replace(&self.forbidden, &self.replacement)
pub struct CensorPlugin {
    pub forbidden: String,
    pub replacement: String,
}

// TODO: impl DataPlugin for UppercasePlugin ...
// TODO: impl DataPlugin for PrefixPlugin ...
// TODO: impl DataPlugin for CensorPlugin ...

// 🎯 TODO 4: Implementiere 'PluginPipeline' mit dynamischem Dispatch (dyn Trait)
// Feld:
// - plugins: Vec<Box<dyn DataPlugin>>
pub struct PluginPipeline {
    pub plugins: Vec<Box<dyn DataPlugin>>,
}

impl PluginPipeline {
    pub fn new() -> Self {
        Self {
            plugins: Vec::new(),
        }
    }

    pub fn register(&mut self, plugin: Box<dyn DataPlugin>) {
        // TODO: Plugin zur Liste hinzufügen
    }

    pub fn count(&self) -> usize {
        self.plugins.len()
    }

    pub fn plugin_names(&self) -> Vec<&str> {
        // TODO: Namen aller Plugins als Vec<&str> sammeln
        Vec::new()
    }

    pub fn execute(&self, input: &str) -> String {
        // TODO: String durch alle Plugins sequentiell leiten und Endergebnis zurückgeben
        input.to_string()
    }
}

fn main() {
    println!("=== Rust 10: Generics & Dynamic Dispatch ===");
    let container = DataContainer::new(100, "sensor-01");
    let transformed = container.transform(|x| x * 2);
    println!("Transformed: {:?} (Val: {})", transformed, transformed.get_value());

    let mut pipeline = PluginPipeline::new();
    // pipeline.register(Box::new(UppercasePlugin));
    println!("Pipeline Plugins: {}", pipeline.count());
}
