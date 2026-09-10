public record Produkt(string Name, decimal Preis, string Kategorie);

public class Aufgabe {
    public static Produkt WendeRabattAn(Produkt original, decimal rabattProzent) {
        return original with { Preis = original.Preis * (1 - rabattProzent / 100m) };
    }
}