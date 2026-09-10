public abstract class Fahrzeug(string marke) {
    public string Marke { get; } = marke;
    public abstract string StarteMotor();
}

public class ElektroAuto(string marke, int batterieKapazitaet) : Fahrzeug(marke) {
    public int BatterieKapazitaet { get; } = batterieKapazitaet;
    public override string StarteMotor() => "Surr... lautloser Elektroantrieb aktiv.";
}