using System.Collections.Generic;
using System.Linq;

public record OrderItem(string ProduktId, int Menge, decimal Einzelpreis);
public record Order(string OrderId, string Kunde, List<OrderItem> Items) {
    public decimal Gesamtsumme => Items.Sum(i => i.Menge * i.Einzelpreis);
}

public class OrderEngine {
    private readonly List<Order> _orders = [];

    public void AddOrder(Order order) => _orders.Add(order);

    public decimal GetGesamtumsatz() => _orders.Sum(o => o.Gesamtsumme);

    public List<Order> GetOrdersVonKunde(string kunde) =>
        _orders.Where(o => o.Kunde == kunde).ToList();
}