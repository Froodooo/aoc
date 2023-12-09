public class App {
    public static void main(String[] args) throws Exception {
        Day09 day09 = new Day09(Utils.readFile("aoc23\\input\\09.txt"));
        System.out.println(day09.partA());
        System.out.println(day09.partB());
    }
}
