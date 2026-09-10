public record Produkt(string Name, decimal Preis, string Kategorie);

public class Aufgabe {
    // 🎯 TEILZIEL 1 (TODO 1): Rabatt anwenden mit with-Expression
    public static Produkt WendeRabattAn(Produkt original, decimal rabattProzent) {
        return original with { Preis = original.Preis * (1 - rabattProzent / 100m) };
    }
}