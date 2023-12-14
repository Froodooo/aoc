import day14.Platform;

public class Day14 {
    private String input;

    public Day14(String input) {
        this.input = input;
    }

    public int partA() {
        Platform platform = new Platform(input);
        platform.tilt(Platform.Direction.NORTH);
        // System.out.println(platform.toString());
        int load = platform.calculateLoad();
        return load;
    }

    public int partB() {
        return -1;
    }
}
