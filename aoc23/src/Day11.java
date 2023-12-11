import day11.Universe;

public class Day11 {
    private String input;
    private int factor;

    public Day11(String input, int factor) {
        this.input = input;
        this.factor = factor;
    }

    public long partA() {
        Universe universe = new Universe(this.input, 1);
        long distance = universe.calculateDistance();
        return distance;
    }

    public long partB() {
        Universe universe = new Universe(this.input, factor);
        long distance = universe.calculateDistance();
        return distance;
    }
}
