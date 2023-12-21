package day21;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

public class Garden {
    String[][] plots;

    private int height;
    private int width;

    private int startX;
    private int startY;

    Set<String> reachable = new HashSet<String>();

    public Garden(String input) {
        String[] lines = input.split("\n");
        plots = new String[lines.length][lines[0].length()];
        height = lines.length;
        width = lines[0].length();

        for (int i = 0; i < lines.length; i++) {
            String[] line = lines[i].split("");
            for (int j = 0; j < line.length; j++) {
                if (line[j].equals("S")) {
                    startX = j;
                    startY = i;
                }
                plots[i][j] = line[j];
            }
        }
    }

    public int reachablePlots(int steps, boolean infinite) {
        Queue<Plot> queue = new ArrayDeque<Plot>();
        queue.add(new Plot(startX, startY));

        while (!queue.isEmpty()) {
            Plot point = queue.poll();

            if (point.getSteps() == steps) {
                continue;
            }

            List<Plot> neighbours = neighbours(point, steps, infinite);
            queue.addAll(neighbours);
        }

        return reachable.size() + 1;
    }

    private List<Plot> neighbours(Plot plot, int steps, boolean infinite) {
        int[] dx = new int[] { 0, 1, 0, -1 };
        int[] dy = new int[] { 1, 0, -1, 0 };

        List<Plot> neighbours = new ArrayList<Plot>();

        for (int i = 0; i < 4; i++) {
            int x = plot.x + dx[i];
            int y = plot.y + dy[i];
            Plot newPlot = new Plot(x, y, plot.getSteps() + 1);
            if (isValid(x, y, infinite)) {
                neighbours.add(newPlot);
                if (newPlot.getSteps() % 2 == 0) {
                    reachable.add(newPlot.toString());
                    // plots[y][x] = "O";
                }
            }
        }
        return neighbours;
    }

    private boolean isValid(int x, int y, boolean infinite) {
        if (!infinite) {
            return x >= 0 && x < plots[0].length && y >= 0 && y < plots.length && plots[y][x].equals(".")
                    && !reachable.contains(new Plot(x, y).toString());
        }

        // if (plots[y][x].equals("O")) {
        // return false;
        // }

        if (reachable.contains(new Plot(x, y).toString())) {
            return false;
        }

        if (x >= 0 && y >= 0) {
            int dx = x % width;
            int dy = y % height;
            return plots[dy][dx].equals(".");
        }
        if (x < 0 && y >= 0) {
            int dx = x % width == 0 ? 0 : (x % width) + width;
            int dy = y % height;
            return plots[dy][dx].equals(".");
        }
        if (x >= 0 && y < 0) {
            int dx = x % width;
            int dy = y % height == 0 ? 0 : (y % height) + height;
            return plots[dy][dx].equals(".");
        }
        if (x < 0 && y < 0) {
            int dx = x % width == 0 ? 0 : (x % width) + width;
            int dy = y % height == 0 ? 0 : (y % height) + height;
            return plots[dy][dx].equals(".");
        }

        throw new RuntimeException("Invalid coordinates");
    }

    public int getStartX() {
        return startX;
    }

    public int getStartY() {
        return startY;
    }

    public String toString() {
        String result = "";

        for (int y = 0; y < plots.length; y++) {
            for (int x = 0; x < plots[0].length; x++) {
                result += reachable.contains(new Plot(x, y).toString()) ? "O" : plots[y][x];
            }
            result += "\n";
        }

        return result;
    }
}
