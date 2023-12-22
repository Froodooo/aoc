public class App {
    public static void main(String[] args) throws Exception {
        Day22 day22 = new Day22(Utils.readFile("aoc23\\input\\22_sample.txt"));
        System.out.println(day22.partA());
        // System.out.println(day22.partB());
    }
}