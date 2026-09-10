using System.Text.Json;

public class Aufgabe {
    public static string SerialisiereZuJson<T>(T obj) => JsonSerializer.Serialize(obj);
    public static T? DeserialisiereAusJson<T>(string json) => JsonSerializer.Deserialize<T>(json);
}