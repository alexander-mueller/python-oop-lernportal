public class Aufgabe {
    public static (int Min, int Max) FindeMinMax(int[] zahlen) {
        int min = int.MaxValue;
        int max = int.MinValue;
        foreach (var z in zahlen) {
            if (z < min) min = z;
            if (z > max) max = z;
        }
        return (min, max);
    }
}