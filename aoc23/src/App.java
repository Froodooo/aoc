public class App {
    public static void main(String[] args) throws Exception {
        Day11 day11 = new Day11(Utils.readFile("aoc23\\input\\11.txt"), 1000000);
        System.out.println(day11.partA());
        System.out.println(day11.partB());
    }
}
