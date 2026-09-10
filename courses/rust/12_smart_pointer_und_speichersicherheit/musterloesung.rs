// ============================================================================
// 🦀 RUST 12: SMART POINTER (MUSTERLÖSUNG)
// ============================================================================

use std::cell::RefCell;
use std::rc::Rc;

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

    pub fn insert(&mut self, new_val: i32) {
        match self {
            TreeNode::Empty => {
                *self = TreeNode::Node {
                    val: new_val,
                    left: Box::new(TreeNode::Empty),
                    right: Box::new(TreeNode::Empty),
                };
            }
            TreeNode::Node { val, left, right } => {
                if new_val < *val {
                    left.insert(new_val);
                } else {
                    right.insert(new_val);
                }
            }
        }
    }

    pub fn contains(&self, target: i32) -> bool {
        match self {
            TreeNode::Empty => false,
            TreeNode::Node { val, left, right } => {
                if target == *val {
                    true
                } else if target < *val {
                    left.contains(target)
                } else {
                    right.contains(target)
                }
            }
        }
    }

    pub fn sum(&self) -> i32 {
        match self {
            TreeNode::Empty => 0,
            TreeNode::Node { val, left, right } => *val + left.sum() + right.sum(),
        }
    }
}

#[derive(Clone)]
pub struct SharedCounter {
    pub inner: Rc<RefCell<i32>>,
}

impl SharedCounter {
    pub fn new(initial: i32) -> Self {
        Self {
            inner: Rc::new(RefCell::new(initial)),
        }
    }

    pub fn clone_handle(&self) -> Self {
        Self {
            inner: Rc::clone(&self.inner),
        }
    }

    pub fn increment(&self, delta: i32) {
        *self.inner.borrow_mut() += delta;
    }

    pub fn get(&self) -> i32 {
        *self.inner.borrow()
    }

    pub fn strong_count(&self) -> usize {
        Rc::strong_count(&self.inner)
    }
}

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

impl Drop for MockResource {
    fn drop(&mut self) {
        self.drop_log
            .borrow_mut()
            .push(format!("Dropped {}", self.name));
    }
}

fn main() {
    println!("=== Rust 12: Smart Pointer & Memory Safety ===");
    let mut tree = TreeNode::new();
    tree.insert(10);
    tree.insert(5);
    tree.insert(15);
    println!("Tree Sum: {}", tree.sum());
    println!("Contains 5: {}", tree.contains(5));
    println!("Contains 99: {}", tree.contains(99));

    let counter = SharedCounter::new(100);
    let c2 = counter.clone_handle();
    c2.increment(25);
    println!("Counter: {} (Handles: {})", counter.get(), counter.strong_count());

    let drop_log = Rc::new(RefCell::new(Vec::new()));
    {
        let _res1 = MockResource::new("DatabaseConn", Rc::clone(&drop_log));
        let _res2 = MockResource::new("FileLock", Rc::clone(&drop_log));
    }
    println!("Drop Log: {:?}", drop_log.borrow());
}
