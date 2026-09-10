package java_course.module12;

import java.util.*;

/**
 * 🧪 TESTSUITE: Java 12 - Lambdas, Streams API & Optional
 */
public class TestAufgabe {

    private static int testsPassed = 0;
    private static int testsTotal = 0;

    private static void assertEquals(Object actual, Object expected, String message) {
        if (actual == null && expected == null) return;
        if (actual == null || !actual.equals(expected)) {
            throw new AssertionError("❌ FAILED: " + message + " (Erwartet: " + expected + ", Erhalten: " + actual + ")");
        }
    }

    private static void assertTrue(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError("❌ FAILED: " + message);
        }
    }

    private static void assertFalse(boolean condition, String message) {
        if (condition) {
            throw new AssertionError("❌ FAILED: " + message);
        }
    }

    private static List<Aufgabe.Employee> createTestData() {
        return List.of(
                new Aufgabe.Employee(1, "Alice Müller", "Engineering", 90000.0, List.of("Java", "AWS", "Docker")),
                new Aufgabe.Employee(2, "Bob Schmidt", "Engineering", 60000.0, List.of("Java", "TypeScript")),
                new Aufgabe.Employee(3, "Carol Weber", "Finance", 80000.0, List.of("Excel", "SAP")),
                new Aufgabe.Employee(4, "David Koch", "Finance", 50000.0, List.of("Excel", "Reporting")),
                new Aufgabe.Employee(5, "Eva Braun", "HR", 55000.0, List.of("Recruiting", "SAP"))
        );
    }

    // @Test
    // TEST: TestStreamBasicsFilterMap - Prüft filter, map, sorted und flatMap
    public static void testStreamBasicsFilterMap() {
        testsTotal++;
        System.out.println("=== RUN   testStreamBasicsFilterMap");
        List<Aufgabe.Employee> team = createTestData();

        List<String> highEarners = Aufgabe.StreamBasics.getHighEarnersNames(team, 75000.0);
        assertEquals(highEarners.size(), 2, "2 Mitarbeiter verdienen >= 75000.0");
        assertEquals(highEarners.get(0), "Alice Müller", "Erster sortierter Name muss Alice sein");
        assertEquals(highEarners.get(1), "Carol Weber", "Zweiter Name Carol");

        Set<String> uniqueSkills = Aufgabe.StreamBasics.extractAllUniqueSkills(team);
        assertTrue(uniqueSkills.contains("Java"), "Skills müssen Java enthalten");
        assertTrue(uniqueSkills.contains("AWS"), "Skills müssen AWS enthalten");
        assertTrue(uniqueSkills.contains("SAP"), "Skills müssen SAP enthalten");
        assertEquals(uniqueSkills.size(), 7, "Insgesamt 7 eindeutige Fähigkeiten");

        testsPassed++;
        System.out.println("--- PASS: testStreamBasicsFilterMap");
    }

    // @Test
    // TEST: TestStreamAggregationsCollectors - Prüft groupingBy, averagingDouble und partitioningBy
    public static void testStreamAggregationsCollectors() {
        testsTotal++;
        System.out.println("=== RUN   testStreamAggregationsCollectors");
        List<Aufgabe.Employee> team = createTestData();

        Map<String, List<Aufgabe.Employee>> grouped = Aufgabe.StreamAggregations.groupByDepartment(team);
        assertEquals(grouped.get("Engineering").size(), 2, "Engineering hat 2 Mitarbeiter");
        assertEquals(grouped.get("Finance").size(), 2, "Finance hat 2 Mitarbeiter");
        assertEquals(grouped.get("HR").size(), 1, "HR hat 1 Mitarbeiter");

        Map<String, Double> avgSalaries = Aufgabe.StreamAggregations.calculateAverageSalaryPerDepartment(team);
        assertEquals(avgSalaries.get("Engineering"), 75000.0, "Engineering Schnitt muss 75000.0 sein");
        assertEquals(avgSalaries.get("Finance"), 65000.0, "Finance Schnitt muss 65000.0 sein");
        assertEquals(avgSalaries.get("HR"), 55000.0, "HR Schnitt muss 55000.0 sein");

        Map<Boolean, List<Aufgabe.Employee>> partitioned = Aufgabe.StreamAggregations.partitionBySeniorSalary(team, 70000.0);
        assertEquals(partitioned.get(true).size(), 2, "2 Personen mit Gehalt >= 70000");
        assertEquals(partitioned.get(false).size(), 3, "3 Personen mit Gehalt < 70000");

        testsPassed++;
        System.out.println("--- PASS: testStreamAggregationsCollectors");
    }

    // @Test
    // TEST: TestOptionalServiceNullSafety - Prüft Optional Pipelines & Exceptions
    public static void testOptionalServiceNullSafety() {
        testsTotal++;
        System.out.println("=== RUN   testOptionalServiceNullSafety");
        List<Aufgabe.Employee> team = createTestData();

        Optional<Aufgabe.Employee> emp1 = Aufgabe.OptionalService.findEmployeeById(team, 1);
        assertTrue(emp1.isPresent(), "Mitarbeiter 1 muss gefunden werden");
        assertEquals(emp1.get().name(), "Alice Müller", "Name muss Alice Müller sein");

        Optional<Aufgabe.Employee> empUnknown = Aufgabe.OptionalService.findEmployeeById(team, 999);
        assertTrue(empUnknown.isEmpty(), "Mitarbeiter 999 existiert nicht (Optional.empty)");

        String deptUpperCase = Aufgabe.OptionalService.getEmployeeDepartmentUpperCase(team, 1);
        assertEquals(deptUpperCase, "ENGINEERING", "Department muss ENGINEERING in Großbuchstaben sein");

        String unknownDept = Aufgabe.OptionalService.getEmployeeDepartmentUpperCase(team, 999);
        assertEquals(unknownDept, "UNKNOWN_DEPARTMENT", "Nicht existierender Mitarbeiter muss UNKNOWN_DEPARTMENT liefern");

        double salary = Aufgabe.OptionalService.getSalaryOrThrow(team, 3);
        assertEquals(salary, 80000.0, "Gehalt von ID 3 muss 80000 sein");

        boolean threwNoSuchElement = false;
        try {
            Aufgabe.OptionalService.getSalaryOrThrow(team, 999);
        } catch (NoSuchElementException e) {
            threwNoSuchElement = true;
        }
        assertTrue(threwNoSuchElement, "getSalaryOrThrow mit ungültiger ID muss NoSuchElementException werfen");

        testsPassed++;
        System.out.println("--- PASS: testOptionalServiceNullSafety");
    }

    public static void main(String[] args) {
        System.out.println("🧪 Führe Java 12 Streams & Optional Testsuite aus...\n----------------------------------------");
        try {
            testStreamBasicsFilterMap();
            testStreamAggregationsCollectors();
            testOptionalServiceNullSafety();
            System.out.println("\n🎉 JUnit 5: Alle " + testsPassed + "/" + testsTotal + " Tests erfolgreich bestanden!");
        } catch (AssertionError e) {
            System.err.println("\n" + e.getMessage());
            System.exit(1);
        }
    }
}
