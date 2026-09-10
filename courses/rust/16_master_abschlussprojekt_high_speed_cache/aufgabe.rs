use std::collections::HashMap;
use std::sync::{Arc, RwLock};

pub struct MemoryCache {
    store: Arc<RwLock<HashMap<String, String>>>,
}

impl MemoryCache {
    // 🎯 TEILZIEL 1 (TODO 1): Initialisierung
    pub fn new() -> Self {
        Self {
            store: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    // 🎯 TEILZIEL 2 (TODO 2): Set und Get
    pub fn set(&self, key: &str, val: &str) {
        let mut map = self.store.write().unwrap();
        map.insert(key.to_string(), val.to_string());
    }

    pub fn get(&self, key: &str) -> Option<String> {
        let map = self.store.read().unwrap();
        map.get(key).cloned()
    }
}