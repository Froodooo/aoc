public class App {
    public static void main(String[] args) throws Exception {
        Day07 day07 = new Day07(Utils.readFile("aoc23\\input\\07.txt"));
        System.out.println("Day 07");
        // System.out.println(day07.partA());
        System.out.println(day07.partB());
    }
}
