public class App {
    public static void main(String[] args) throws Exception {
        Day10 day10 = new Day10(Utils.readFile("aoc23\\input\\10.txt"));
        System.out.println(day10.partA());
        // System.out.println(day10.partB());
    }
}
