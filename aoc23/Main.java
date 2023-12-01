package aoc23;

public class Main {
    public static void main(String[] args) {
        Day01 day01 = new Day01(Utils.readFile("01.txt"));
        day01.partA();
        day01.partB();
    }
}
