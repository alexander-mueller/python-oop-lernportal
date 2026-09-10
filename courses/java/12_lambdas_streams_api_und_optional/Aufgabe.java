package java_course.module12;

import java.util.*;
import java.util.stream.Collectors;

/**
 * ☕ JAVA 12: LAMBDAS, STREAMS API & OPTIONAL
 * ===========================================
 * In diesem Modul meisterst du funktionale Programmierung und deklarative Datenverarbeitung
 * in modernem Java: Lambdas, Methodenreferenzen (::), Streams Pipelines, mächtige
 * Collector-Aggregationen und Null-Safety mit Optional<T>.
 */
public class Aufgabe {

    // ========================================================================
    // 🎯 MODEL: Employee & Department Record
    // ========================================================================
    public record Employee(int id, String name, String department, double salary, List<String> skills) {
        public Employee {
            Objects.requireNonNull(name, "Name darf nicht null sein");
            Objects.requireNonNull(department, "Department darf nicht null sein");
            if (skills == null) skills = List.of();
        }
    }

    // ========================================================================
    // 🎯 TODO 1: Basis-Filterung & Transformation mit Streams
    // ========================================================================
    // Implementiere die folgenden statischen Analysemethoden.
    //
    // Anforderungen:
    // 1. 'public static List<String> getHighEarnersNames(List<Employee> employees, double minSalary)'
    //    - Filtert Mitarbeiter mit Gehalt >= minSalary.
    //    - Mappt auf deren Namen.
    //    - Sortiert alphabetisch.
    //    - Gibt eine Liste zurück (Collectors.toList() oder .toList()).
    //
    // 2. 'public static Set<String> extractAllUniqueSkills(List<Employee> employees)'
    //    - Extrahiert alle Fähigkeiten (skills) aller Mitarbeiter mittels flatMap.
    //    - Liefert ein Set aller eindeutigen Skills.
    public static class StreamBasics {

        public static List<String> getHighEarnersNames(List<Employee> employees, double minSalary) {
            // TODO: Stream-Pipeline: filter -> map -> sorted -> toList
            return List.of();
        }

        public static Set<String> extractAllUniqueSkills(List<Employee> employees) {
            // TODO: flatMap über skills -> collect toSet
            return Set.of();
        }
    }

    // ========================================================================
    // 🎯 TODO 2: Mächtige Aggregationen mit Collectors
    // ========================================================================
    // Implementiere Abteilungsstatistiken mit Java Streams Collectors.
    //
    // Anforderungen:
    // 1. 'public static Map<String, List<Employee>> groupByDepartment(List<Employee> employees)'
    //    - Gruppiert alle Mitarbeiter nach ihrem Department (Collectors.groupingBy).
    //
    // 2. 'public static Map<String, Double> calculateAverageSalaryPerDepartment(List<Employee> employees)'
    //    - Berechnet das durchschnittliche Gehalt je Abteilung (Collectors.groupingBy mit Collectors.averagingDouble).
    //
    // 3. 'public static Map<Boolean, List<Employee>> partitionBySeniorSalary(List<Employee> employees, double threshold)'
    //    - Teilt die Belegschaft in zwei Gruppen: >= threshold (true) und < threshold (false)
    //      mittels Collectors.partitioningBy.
    public static class StreamAggregations {

        public static Map<String, List<Employee>> groupByDepartment(List<Employee> employees) {
            // TODO: groupingBy Department
            return Map.of();
        }

        public static Map<String, Double> calculateAverageSalaryPerDepartment(List<Employee> employees) {
            // TODO: groupingBy mit averagingDouble
            return Map.of();
        }

        public static Map<Boolean, List<Employee>> partitionBySeniorSalary(List<Employee> employees, double threshold) {
            // TODO: partitioningBy Gehalt >= threshold
            return Map.of();
        }
    }

    // ========================================================================
    // 🎯 TODO 3: Null-Safety & Verkettung mit Optional<T>
    // ========================================================================
    // Implementiere sichere Datenabfragen ohne NullPointerExceptions.
    //
    // Anforderungen:
    // 1. 'public static Optional<Employee> findEmployeeById(List<Employee> employees, int id)'
    //    - Sucht den Mitarbeiter per id (filter -> findFirst).
    //
    // 2. 'public static String getEmployeeDepartmentUpperCase(List<Employee> employees, int id)'
    //    - Findet den Mitarbeiter per id, mappt das Department zu UpperCase (department.toUpperCase())
    //    - Gibt "UNKNOWN_DEPARTMENT" zurück, falls der Mitarbeiter nicht existiert (orElse).
    //
    // 3. 'public static double getSalaryOrThrow(List<Employee> employees, int id)'
    //    - Findet den Mitarbeiter per id und liefert dessen Gehalt.
    //    - Wirft NoSuchElementException("Mitarbeiter nicht gefunden: " + id), falls nicht vorhanden.
    public static class OptionalService {

        public static Optional<Employee> findEmployeeById(List<Employee> employees, int id) {
            // TODO: filter & findFirst
            return Optional.empty();
        }

        public static String getEmployeeDepartmentUpperCase(List<Employee> employees, int id) {
            // TODO: findEmployeeById -> map(Department::toUpperCase) -> orElse
            return "";
        }

        public static double getSalaryOrThrow(List<Employee> employees, int id) {
            // TODO: findEmployeeById -> map(salary) -> orElseThrow
            return 0.0;
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 12: Lambdas, Streams API & Optional");
        System.out.println("--------------------------------------------");

        List<Employee> team = List.of(
                new Employee(1, "Alice Müller", "Engineering", 85000.0, List.of("Java", "Cloud", "Docker")),
                new Employee(2, "Bob Schmidt", "Engineering", 72000.0, List.of("Java", "React")),
                new Employee(3, "Carol Weber", "Finance", 92000.0, List.of("Controlling", "Excel")),
                new Employee(4, "David Koch", "HR", 55000.0, List.of("Recruiting", "Communication"))
        );

        List<String> topEarners = StreamBasics.getHighEarnersNames(team, 75000.0);
        System.out.println("Top Earners: " + topEarners);

        Map<String, Double> avgSalaries = StreamAggregations.calculateAverageSalaryPerDepartment(team);
        System.out.println("Avg Salaries: " + avgSalaries);

        String dept = OptionalService.getEmployeeDepartmentUpperCase(team, 1);
        System.out.println("Department von ID 1: " + dept);
    }
}
