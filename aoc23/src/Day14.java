import day14.Platform;

public class Day14 {
    private String input;

    public Day14(String input) {
        this.input = input;
    }

    public int partA() {
        Platform platform = new Platform(input);
        platform.tilt();
        int load = platform.calculateLoad();
        return load;
    }

    public int partB() {
        Platform platform = new Platform(input);
        for (int j = 0; j < 1000; j++) {
            for (int i = 0; i < 4; i++) {
                platform.tilt();
                platform.rotate();
                platform.sort();
            }
        }

        // Manual calculation:
        // from start: skip 86
        // pattern: 52 numbers
        // number of whole patterns: 19230767
        // (19230767 * 52) + 86 = 999999970
        // So walk 30 steps from start of pattern, will end up at 100310

        return -1;
    }
}
