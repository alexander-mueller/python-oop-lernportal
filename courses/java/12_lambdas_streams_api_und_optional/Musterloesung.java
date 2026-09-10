package java_course.module12;

import java.util.*;
import java.util.stream.Collectors;

/**
 * ☕ JAVA 12: LAMBDAS, STREAMS API & OPTIONAL - MUSTERLÖSUNG
 * ==========================================================
 */
public class Musterloesung {

    public record Employee(int id, String name, String department, double salary, List<String> skills) {
        public Employee {
            Objects.requireNonNull(name, "Name darf nicht null sein");
            Objects.requireNonNull(department, "Department darf nicht null sein");
            if (skills == null) skills = List.of();
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 1: StreamBasics
    // ========================================================================
    public static class StreamBasics {

        public static List<String> getHighEarnersNames(List<Employee> employees, double minSalary) {
            if (employees == null) return List.of();
            return employees.stream()
                    .filter(e -> e.salary() >= minSalary)
                    .map(Employee::name)
                    .sorted()
                    .collect(Collectors.toList());
        }

        public static Set<String> extractAllUniqueSkills(List<Employee> employees) {
            if (employees == null) return Set.of();
            return employees.stream()
                    .flatMap(e -> e.skills().stream())
                    .collect(Collectors.toSet());
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 2: StreamAggregations
    // ========================================================================
    public static class StreamAggregations {

        public static Map<String, List<Employee>> groupByDepartment(List<Employee> employees) {
            if (employees == null) return Map.of();
            return employees.stream()
                    .collect(Collectors.groupingBy(Employee::department));
        }

        public static Map<String, Double> calculateAverageSalaryPerDepartment(List<Employee> employees) {
            if (employees == null) return Map.of();
            return employees.stream()
                    .collect(Collectors.groupingBy(
                            Employee::department,
                            Collectors.averagingDouble(Employee::salary)
                    ));
        }

        public static Map<Boolean, List<Employee>> partitionBySeniorSalary(List<Employee> employees, double threshold) {
            if (employees == null) return Map.of();
            return employees.stream()
                    .collect(Collectors.partitioningBy(e -> e.salary() >= threshold));
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 3: OptionalService
    // ========================================================================
    public static class OptionalService {

        public static Optional<Employee> findEmployeeById(List<Employee> employees, int id) {
            if (employees == null) return Optional.empty();
            return employees.stream()
                    .filter(e -> e.id() == id)
                    .findFirst();
        }

        public static String getEmployeeDepartmentUpperCase(List<Employee> employees, int id) {
            return findEmployeeById(employees, id)
                    .map(Employee::department)
                    .map(String::toUpperCase)
                    .orElse("UNKNOWN_DEPARTMENT");
        }

        public static double getSalaryOrThrow(List<Employee> employees, int id) {
            return findEmployeeById(employees, id)
                    .map(Employee::salary)
                    .orElseThrow(() -> new NoSuchElementException("Mitarbeiter nicht gefunden: " + id));
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 12: Streams API & Optional (Musterlösung)");
        System.out.println("-------------------------------------------------");

        List<Employee> team = List.of(
                new Employee(1, "Alice Müller", "Engineering", 85000.0, List.of("Java", "Cloud", "Docker")),
                new Employee(2, "Bob Schmidt", "Engineering", 72000.0, List.of("Java", "React")),
                new Employee(3, "Carol Weber", "Finance", 92000.0, List.of("Controlling", "Excel")),
                new Employee(4, "David Koch", "HR", 55000.0, List.of("Recruiting", "Communication"))
        );

        System.out.println("Top Earners: " + StreamBasics.getHighEarnersNames(team, 75000.0));
        System.out.println("All Skills: " + StreamBasics.extractAllUniqueSkills(team));
        System.out.println("Avg Salaries: " + StreamAggregations.calculateAverageSalaryPerDepartment(team));
        System.out.println("Department ID 1: " + OptionalService.getEmployeeDepartmentUpperCase(team, 1));
    }
}
