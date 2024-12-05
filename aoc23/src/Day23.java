import day23.Trail;

public class Day23 {
    private String input;

    public Day23(String input) {
        this.input = input;
    }

    public int partA() {
        Trail trail = new Trail(input);
        System.out.println(trail.toString());
        System.out.println(trail.getEntry());
        System.out.println(trail.getExit());

        int steps = trail.walk();
        System.out.println(steps);
        return -1;
    }

    public long partB() {
        return -1;
    }
}