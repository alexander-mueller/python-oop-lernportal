#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

std::mutex g_mutex;
int g_zaehler = 0;

void erhoehe_zaehler() {
    std::lock_guard<std::mutex> lock(g_mutex);
    g_zaehler++;
}