public class App {
    public static void main(String[] args) throws Exception {
        Day12 day12 = new Day12(Utils.readFile("aoc23\\input\\12.txt"));
        System.out.println(day12.partA());
        // System.out.println(day12.partB());
    }
}
