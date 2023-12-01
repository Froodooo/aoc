public class App {
    public static void main(String[] args) throws Exception {
        Day01 day01 = new Day01(Utils.readFile("aoc23\\input\\01.txt"));
        System.out.println("Day 01");
        System.out.println(day01.partA());
        System.out.println(day01.partB());
    }
}
