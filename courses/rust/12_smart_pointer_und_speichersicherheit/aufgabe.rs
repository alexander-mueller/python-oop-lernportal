// ============================================================================
// 🦀 RUST 12: SMART POINTER (BOX, RC, REFCELL)
// ============================================================================

use std::cell::RefCell;
use std::rc::Rc;

// 🎯 TODO 1: Implementiere den rekursiven Binärbaum 'TreeNode' mit Box<T>
#[derive(Debug, PartialEq)]
pub enum TreeNode {
    Empty,
    Node {
        val: i32,
        left: Box<TreeNode>,
        right: Box<TreeNode>,
    },
}

impl TreeNode {
    pub fn new() -> Self {
        TreeNode::Empty
    }

    // Fügt einen Wert in den binären Suchbaum ein (kleinere Werte links, größere/gleiche rechts)
    pub fn insert(&mut self, new_val: i32) {
        // TODO: Muster-Matching auf &mut self; falls Empty -> Node erzeugen; falls Node -> rekursiv absteigen
    }

    // Prüft, ob der Wert im Baum existiert
    pub fn contains(&self, target: i32) -> bool {
        // TODO: Rekursive Suche
        false
    }

    // Berechnet die Summe aller Knotenwerte
    pub fn sum(&self) -> i32 {
        // TODO: Summe berechnen
        0
    }
}

// 🎯 TODO 2: Implementiere 'SharedCounter' mit Rc<RefCell<i32>>
// Erlaubt geteilten veränderlichen Zugriff im Single-Thread
#[derive(Clone)]
pub struct SharedCounter {
    pub inner: Rc<RefCell<i32>>,
}

impl SharedCounter {
    pub fn new(initial: i32) -> Self {
        // TODO: Rc::new(RefCell::new(initial)) verpacken
        Self {
            inner: Rc::new(RefCell::new(initial)),
        }
    }

    pub fn clone_handle(&self) -> Self {
        // TODO: Rc klonen (erhöht Reference Count)
        Self {
            inner: Rc::clone(&self.inner),
        }
    }

    pub fn increment(&self, delta: i32) {
        // TODO: Über borrow_mut() den internen Wert um delta erhöhen
    }

    pub fn get(&self) -> i32 {
        // TODO: Über borrow() den internen Wert auslesen
        0
    }

    pub fn strong_count(&self) -> usize {
        // TODO: Rc::strong_count(&self.inner) liefern
        0
    }
}

// 🎯 TODO 3: Implementiere 'MockResource' mit RAII Drop Trait
pub struct MockResource {
    pub name: String,
    pub drop_log: Rc<RefCell<Vec<String>>>,
}

impl MockResource {
    pub fn new(name: &str, drop_log: Rc<RefCell<Vec<String>>>) -> Self {
        Self {
            name: name.to_string(),
            drop_log,
        }
    }
}

// TODO: impl Drop for MockResource
// Beim Droppen soll "Dropped <name>" an self.drop_log angehängt werden!

fn main() {
    println!("=== Rust 12: Smart Pointer & Memory Safety ===");
    let mut tree = TreeNode::new();
    tree.insert(10);
    tree.insert(5);
    tree.insert(15);
    println!("Tree Sum: {}", tree.sum());

    let counter = SharedCounter::new(100);
    let c2 = counter.clone_handle();
    c2.increment(25);
    println!("Counter: {} (Handles: {})", counter.get(), counter.strong_count());
}
