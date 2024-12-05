public class App {
    public static void main(String[] args) throws Exception {
        Day23 day23 = new Day23(Utils.readFile("aoc23\\input\\23_sample.txt"));
        System.out.println(day23.partA());
        // System.out.println(day23.partB());
    }
}