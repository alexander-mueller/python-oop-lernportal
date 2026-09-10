using System;

public class Aufgabe {
    public static int FuehreAus(Func<int, int, int> operation, int a, int b) => operation(a, b);
}