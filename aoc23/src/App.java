public class App {
    public static void main(String[] args) throws Exception {
        Day01 day01 = new Day01(Utils.readFile("aoc23\\input\\01.txt"));
        System.out.println("Day 01");
        System.out.println(day01.partA());
        System.out.println(day01.partB());

        Day02 day02 = new Day02(Utils.readFile("aoc23\\input\\02.txt"));
        System.out.println("Day 02");
        System.out.println(day02.partA());
        System.out.println(day02.partB());
    }
}