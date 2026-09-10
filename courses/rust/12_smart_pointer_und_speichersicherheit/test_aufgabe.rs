// ============================================================================
// 🧪 TESTSUITE: RUST 12 SMART POINTER (BOX, RC, REFCELL)
// ============================================================================

#[allow(dead_code)]
#[path = "aufgabe.rs"]
mod aufgabe;

#[allow(unused_imports)]
use aufgabe::*;
use std::cell::RefCell;
use std::rc::Rc;

// TEST: test_tree_node_box
#[test]
fn test_tree_node_box() {
    let mut tree = TreeNode::new();
    assert_eq!(tree.sum(), 0);
    assert_eq!(tree.contains(10), false);

    tree.insert(50);
    tree.insert(25);
    tree.insert(75);
    tree.insert(10);
    tree.insert(30);

    assert_eq!(tree.sum(), 190);
    assert!(tree.contains(50));
    assert!(tree.contains(25));
    assert!(tree.contains(75));
    assert!(tree.contains(10));
    assert!(tree.contains(30));
    assert_eq!(tree.contains(999), false);
}

// TEST: test_shared_counter_rc_refcell
#[test]
fn test_shared_counter_rc_refcell() {
    let counter = SharedCounter::new(10);
    assert_eq!(counter.get(), 10);
    assert_eq!(counter.strong_count(), 1);

    let handle_a = counter.clone_handle();
    let handle_b = counter.clone_handle();
    assert_eq!(counter.strong_count(), 3);

    handle_a.increment(15);
    assert_eq!(counter.get(), 25);
    assert_eq!(handle_b.get(), 25);

    handle_b.increment(-5);
    assert_eq!(counter.get(), 20);

    drop(handle_a);
    assert_eq!(counter.strong_count(), 2);
}

// TEST: test_raii_drop_cleanup
#[test]
fn test_raii_drop_cleanup() {
    let log = Rc::new(RefCell::new(Vec::new()));

    {
        let _r1 = MockResource::new("Socket_A", Rc::clone(&log));
        let _r2 = MockResource::new("Socket_B", Rc::clone(&log));
        assert_eq!(log.borrow().len(), 0);
    } // Hier werden _r2 und _r1 gedroppt (in umgekehrter Reihenfolge)

    let entries = log.borrow();
    assert_eq!(entries.len(), 2);
    assert!(entries.contains(&"Dropped Socket_A".to_string()));
    assert!(entries.contains(&"Dropped Socket_B".to_string()));
}

fn main() {
    println!("🧪 Führe Rust 12 Testsuite aus...");
    test_tree_node_box();
    println!("  ✓ test_tree_node_box bestanden");
    test_shared_counter_rc_refcell();
    println!("  ✓ test_shared_counter_rc_refcell bestanden");
    test_raii_drop_cleanup();
    println!("  ✓ test_raii_drop_cleanup bestanden");
    println!("\n✅ Alle Tests für Rust 12 erfolgreich bestanden!");
}
