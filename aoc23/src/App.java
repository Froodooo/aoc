public class App {
    public static void main(String[] args) throws Exception {
        Day08 day08 = new Day08(Utils.readFile("aoc23\\input\\08.txt"));
        System.out.println("Day 08");
        System.out.println(day08.partA());
        System.out.println(day08.partB());
    }
}
