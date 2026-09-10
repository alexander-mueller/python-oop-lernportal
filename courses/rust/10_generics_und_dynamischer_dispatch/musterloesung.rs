// ============================================================================
// 🦀 RUST 10: GENERICS & DYNAMISCHER DISPATCH (MUSTERLÖSUNG)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
pub struct DataContainer<T> {
    pub value: T,
    pub tag: String,
}

impl<T> DataContainer<T> {
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
        let new_val = op(self.value);
        DataContainer {
            value: new_val,
            tag: self.tag,
        }
    }
}

pub trait DataPlugin {
    fn name(&self) -> &str;
    fn process(&self, input: &str) -> String;
}

pub struct UppercasePlugin;

impl DataPlugin for UppercasePlugin {
    fn name(&self) -> &str {
        "uppercase"
    }

    fn process(&self, input: &str) -> String {
        input.to_uppercase()
    }
}

pub struct PrefixPlugin {
    pub prefix: String,
}

impl DataPlugin for PrefixPlugin {
    fn name(&self) -> &str {
        "prefix"
    }

    fn process(&self, input: &str) -> String {
        format!("{}{}", self.prefix, input)
    }
}

pub struct CensorPlugin {
    pub forbidden: String,
    pub replacement: String,
}

impl DataPlugin for CensorPlugin {
    fn name(&self) -> &str {
        "censor"
    }

    fn process(&self, input: &str) -> String {
        input.replace(&self.forbidden, &self.replacement)
    }
}

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
        self.plugins.push(plugin);
    }

    pub fn count(&self) -> usize {
        self.plugins.len()
    }

    pub fn plugin_names(&self) -> Vec<&str> {
        self.plugins.iter().map(|p| p.name()).collect()
    }

    pub fn execute(&self, input: &str) -> String {
        let mut current = input.to_string();
        for plugin in &self.plugins {
            current = plugin.process(&current);
        }
        current
    }
}

fn main() {
    println!("=== Rust 10: Generics & Dynamic Dispatch ===");
    let container = DataContainer::new(100, "sensor-01");
    let transformed = container.transform(|x| x * 2);
    println!("Transformed: {:?} (Val: {})", transformed, transformed.get_value());

    let mut pipeline = PluginPipeline::new();
    pipeline.register(Box::new(PrefixPlugin { prefix: ">> ".to_string() }));
    pipeline.register(Box::new(UppercasePlugin));
    pipeline.register(Box::new(CensorPlugin {
        forbidden: "GEHEIM".to_string(),
        replacement: "******".to_string(),
    }));

    let output = pipeline.execute("hallo geheim welt");
    println!("Pipeline Output: '{}'", output);
}
