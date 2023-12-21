import day21.Garden;

public class Day21 {
    private String input;

    public Day21(String input) {
        this.input = input;
    }

    public int partA() {
        Garden garden = new Garden(input);
        int reachable = garden.reachablePlots(64, false);
        System.out.println(garden.toString());
        return reachable;
    }

    public long partB() {
        Garden garden = new Garden(input);
        int reachable = garden.reachablePlots(129, false);
        System.out.println(garden.toString());
        return reachable;
    }
}