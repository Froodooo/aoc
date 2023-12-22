package day22;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Snapshot {
    List<Brick> bricks;

    public Snapshot(String input) {
        bricks = new ArrayList<>();
        for (String line : input.split("\n")) {
            bricks.add(new Brick(line));
        }
        Collections.sort(bricks);
    }

    public void fall() {
        boolean changed = false;
        do {
        } while (changed);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Brick brick : bricks) {
            sb.append(brick.toString());
            sb.append("\n");
        }
        return sb.toString();
    }
}
