package day22;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Snapshot {
    List<Brick> bricks;

    public Snapshot(String input) {
        bricks = new ArrayList<>();
        for (String line : input.split("\n")) {
            bricks.add(new Brick(line));
        }
        Collections.sort(bricks);
    }

    public void drop() {
        List<Brick> droppedBricks = new ArrayList<>();
        Map<Integer, Integer> xMap = new HashMap<>();
        Map<Integer, Integer> yMap = new HashMap<>();
        
        for (Brick brick : bricks) {
            int highestX = 0;
            for (int x = brick.xMin; x <= brick.xMax; x++) {
                if (xMap.containsKey(x)) {
                    highestX = Math.max(highestX, xMap.get(x));
                } else {
                    xMap.put(x, brick.zMax);
                }
            }
            int highestY = 0;
            for (int y = brick.yMin; y <= brick.yMax; y++) {
                if (yMap.containsKey(y)) {
                    highestY = Math.max(highestY, yMap.get(y));
                } else {
                    yMap.put(y, brick.zMax);
                }
            }

            
        }

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
