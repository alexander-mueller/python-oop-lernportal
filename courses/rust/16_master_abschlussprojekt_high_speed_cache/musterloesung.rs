use std::collections::HashMap;
use std::sync::{Arc, RwLock};

pub struct MemoryCache {
    store: Arc<RwLock<HashMap<String, String>>>,
}

impl MemoryCache {
    pub fn new() -> Self {
        Self {
            store: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    pub fn set(&self, key: &str, val: &str) {
        let mut map = self.store.write().unwrap();
        map.insert(key.to_string(), val.to_string());
    }

    pub fn get(&self, key: &str) -> Option<String> {
        let map = self.store.read().unwrap();
        map.get(key).cloned()
    }
}