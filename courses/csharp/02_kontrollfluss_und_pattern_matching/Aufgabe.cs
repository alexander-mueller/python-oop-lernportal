public class Aufgabe {
    // 🎯 TEILZIEL 1 (TODO 1): Kategorisiere Temperatur mit Switch-Expression
    public static string BewerteTemperatur(double gradCelsius) =>
        gradCelsius switch {
            < 0 => "Frost",
            >= 0 and < 15 => "Kühl",
            >= 15 and < 25 => "Angenehm",
            _ => "Heiß"
        };
}