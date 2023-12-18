package day18;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.awt.Point;
import java.awt.Polygon;

public class Terrain {
    private int minWidth;
    private int maxWidth;
    private int minHeight;
    private int maxHeight;

    private int x;
    private int y;

    private List<Point> trenches;
    private Polygon polygon;

    public Terrain(String input) {
        this(input, false);
    }

    public Terrain(String input, boolean isHex) {
        minWidth = Integer.MAX_VALUE;
        maxWidth = Integer.MIN_VALUE;
        minHeight = Integer.MAX_VALUE;
        maxHeight = Integer.MIN_VALUE;
        x = 0;
        y = 0;
        trenches = new ArrayList<Point>();
        polygon = new Polygon();
        polygon.addPoint(0, 0);

        String[] lines = input.split("\n");
        for (String line : lines) {
            Instruction instruction = new Instruction(line, isHex);
            move(instruction);
            updateBounds();
        }
    }

    // https://www.geeksforgeeks.org/area-of-a-polygon-with-given-n-ordered-vertices/
    private double shoelace(double X[], double Y[], int n) {
        // Initialize area
        double area = 0.0;

        // Calculate value of shoelace formula
        int j = n - 1;
        for (int i = 0; i < n; i++) {
            area += (X[j] + X[i]) * (Y[j] - Y[i]);

            // j is previous vertex to i
            j = i;
        }

        // Return absolute value
        return Math.abs(area / 2.0);
    }

    public long calculateCubicMeters() {
        return (long) shoelace(Arrays.stream(polygon.xpoints).asDoubleStream().toArray(),
                Arrays.stream(polygon.ypoints).asDoubleStream().toArray(), polygon.npoints) + (trenches.size() / 2) + 1;
    }

    private void move(Instruction instruction) {
        switch (instruction.getDirection()) {
            case UP:
                for (int i = 0; i < instruction.getMeters(); i++) {
                    trenches.add(new Point(x, y - i));
                }
                polygon.addPoint(x, y - instruction.getMeters());
                y -= instruction.getMeters();
                break;
            case DOWN:
                for (int i = 0; i < instruction.getMeters(); i++) {
                    trenches.add(new Point(x, y + i));
                }
                polygon.addPoint(x, y + instruction.getMeters());
                y += instruction.getMeters();
                break;
            case LEFT:
                for (int i = 0; i < instruction.getMeters(); i++) {
                    trenches.add(new Point(x - i, y));
                }
                polygon.addPoint(x - instruction.getMeters(), y);
                x -= instruction.getMeters();
                break;
            case RIGHT:
                for (int i = 0; i < instruction.getMeters(); i++) {
                    trenches.add(new Point(x + i, y));
                }
                polygon.addPoint(x + instruction.getMeters(), y);
                x += instruction.getMeters();
                break;
            default:
                throw new IllegalArgumentException("Invalid direction: " + instruction.getDirection());
        }
    }

    private void updateBounds() {
        if (x < minWidth) {
            minWidth = x;
        }
        if (x > maxWidth) {
            maxWidth = x;
        }
        if (y < minHeight) {
            minHeight = y;
        }
        if (y > maxHeight) {
            maxHeight = y;
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int y = minHeight; y <= maxHeight; y++) {
            for (int x = minWidth; x <= maxWidth; x++) {
                final int xx = x;
                final int yy = y;
                if (trenches.stream().filter(trench -> trench.getX() == xx && trench.getY() == yy).findFirst()
                        .isPresent()) {
                    sb.append("#");
                } else {
                    sb.append(".");
                }
            }
            sb.append("\n");
        }
        return sb.toString();
    }
}
