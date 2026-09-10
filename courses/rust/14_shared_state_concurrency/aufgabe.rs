use std::sync::{Arc, Mutex};
use std::thread;

// 🎯 TEILZIEL 1 (TODO 1): Zähler über Threads hinweg inkrementieren
pub fn paralleler_zaehler(thread_anzahl: usize) -> i32 {
    let zaehler = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..thread_anzahl {
        let z = Arc::clone(&zaehler);
        let handle = thread::spawn(move || {
            let mut num = z.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for h in handles {
        h.join().unwrap();
    }

    let final_val = *zaehler.lock().unwrap();
    final_val
}