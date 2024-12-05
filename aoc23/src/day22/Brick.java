package day22;

import java.util.Arrays;

public class Brick implements Comparable<Brick> {
    int xMin;
    int xMax;
    int yMin;
    int yMax;
    int zMin;
    int zMax;

    public Brick(String input) {
        String[] parts = input.split("~");
        int[] min = Arrays.asList(parts[0].split(",")).stream().mapToInt(Integer::parseInt).toArray();
        int[] max = Arrays.asList(parts[1].split(",")).stream().mapToInt(Integer::parseInt).toArray();
        xMin = min[0];
        xMax = max[0];
        yMin = min[1];
        yMax = max[1];
        zMin = min[2];
        zMax = max[2];
    }

    public String toString() {
        return String.format("%d,%d,%d~%d,%d,%d", xMin, yMin, zMin, xMax, yMax, zMax);
    }

    @Override
    public int compareTo(Brick o) {
        return Integer.compare(this.zMin, o.zMin);
    }
}
