import day18.Terrain;

public class Day18 {
    private String input;

    public Day18(String input) {
        this.input = input;

    }

    public long partA() {
        Terrain terrain = new Terrain(input);
        return terrain.calculateCubicMeters();
    }

    public long partB() {
        Terrain terrain = new Terrain(input, true);
        return terrain.calculateCubicMeters();
    }
}