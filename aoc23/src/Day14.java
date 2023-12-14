import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import day14.Platform;
import day14.Platform.Direction;

public class Day14 {
    private String input;

    public Day14(String input) {
        this.input = input;
    }

    public int partA() {
        Platform platform = new Platform(input);
        platform.tilt(Platform.Direction.NORTH);
        int load = platform.calculateLoad();
        return load;
    }

    public int partB() {
        Platform platform = new Platform(input);
        for (int j = 0; j < 1000; j++) {
            for (int i = 0; i < 4; i++) {
                platform.tilt(Platform.Direction.NORTH);
                platform.rotate(Direction.WEST);
                platform.sort();
            }
            // System.out.println(platform.calculateLoad());

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
