public class App {
    public static void main(String[] args) throws Exception {
        Day21 day21 = new Day21(Utils.readFile("aoc23\\input\\21.txt"));
        System.out.println(day21.partA());
        // System.out.println(day21.partB());
    }
}