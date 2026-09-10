public class Kunde(string name, string email) {
    public string Name { get; } = name;
    public string Email { get; init; } = email;
    public decimal Guthaben { get; private set; } = 0.0m;

    // 🎯 TEILZIEL 1 (TODO 1): Guthaben aufladen
    public void LadeGuthaben(decimal betrag) {
        if (betrag > 0) Guthaben += betrag;
    }
}