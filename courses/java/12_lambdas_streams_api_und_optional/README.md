# ☕ Java 12: Lambdas, Streams API & Optional

Mit **Java 8** und den Weiterentwicklungen bis **Java 21+** hat sich Java von einer rein imperativen zu einer modernen multi-paradigmatischen Sprache mit mächtiger funktionaler Datenverarbeitung gewandelt.

---

## 🌊 1. Die Anatomie einer Stream-Pipeline

Eine Stream-Pipeline besteht immer aus drei Schritten:

```
[Datenquelle] ───> [Intermediäre Operationen (Lazy)] ───> [Terminale Operation (Eager)]
(Collection, Array) (filter, map, sorted, flatMap)       (collect, count, reduce, forEach)
```

### Beispiel:
```java
List<String> topPerformers = employees.stream()
    .filter(e -> e.salary() > 80000)        // 1. Filtern
    .map(Employee::name)                     // 2. Transformieren (Method Reference)
    .sorted()                                // 3. Sortieren
    .limit(5)                                // 4. Begrenzen
    .toList();                               // 5. Sammeln in Liste (Java 16+)
```

---

## 📊 2. Fortgeschrittene Collector-Aggregationen

Mit `java.util.stream.Collectors` lassen sich komplexe SQL-ähnliche Aggregationen deklarativ und parallelisierbar formulieren:

```java
// Gruppierung nach Abteilung:
Map<String, List<Employee>> byDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::department));

// Durchschnittsgehalt je Abteilung:
Map<String, Double> avgSalary = employees.stream()
    .collect(Collectors.groupingBy(
        Employee::department,
        Collectors.averagingDouble(Employee::salary)
    ));

// Partitionierung in zwei disjunkte Gruppen (true / false):
Map<Boolean, List<Employee>> seniors = employees.stream()
    .collect(Collectors.partitioningBy(e -> e.salary() >= 100_000));
```

---

## 🛡️ 3. Null-Safety mit `Optional<T>`

`Optional<T>` eliminiert gefürchtete `NullPointerException`s (die "Billion Dollar Mistake") durch funktionale Ketten:

```java
// Statt: if (emp != null && emp.getDept() != null) ...
String deptName = Optional.ofNullable(employee)
    .map(Employee::department)
    .map(String::toUpperCase)
    .orElse("DEFAULT_DEPT");
```

---

## 🎯 Aufgabenübersicht (`Aufgabe.java`)

1. **TODO 1:** `StreamBasics` mit `getHighEarnersNames(...)` und `extractAllUniqueSkills(...)` (via `flatMap`).
2. **TODO 2:** `StreamAggregations` mit `groupByDepartment(...)`, `calculateAverageSalaryPerDepartment(...)` und `partitionBySeniorSalary(...)`.
3. **TODO 3:** `OptionalService` mit `findEmployeeById(...)`, `getEmployeeDepartmentUpperCase(...)` und `getSalaryOrThrow(...)`.
