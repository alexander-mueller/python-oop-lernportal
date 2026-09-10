using System.Collections.Generic;

public class Aufgabe {
    public static List<int> FiltereGeradeZahlen(int[] zahlen) {
        var res = new List<int>();
        foreach (var z in zahlen) {
            if (z % 2 == 0) res.Add(z);
        }
        return res;
    }
}