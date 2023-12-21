package day21;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

public class Garden {
    String[][] plots;
    private int startX;
    private int startY;

    public Garden(String input) {
        String[] lines = input.split("\n");
        plots = new String[lines.length][lines[0].length()];

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

    public int reachablePlots(int steps) {
        Queue<Plot> queue = new ArrayDeque<Plot>();
        queue.add(new Plot(startX, startY));

        while (!queue.isEmpty()) {
            Plot point = queue.poll();

            if (point.getSteps() == steps) {
                continue;
            }

            List<Plot> neighbours = neighbours(point, steps);
            queue.addAll(neighbours);
        }

        return countReachable() + 1;
    }

    private List<Plot> neighbours(Plot plot, int steps) {
        int[] dx = new int[] { 0, 1, 0, -1 };
        int[] dy = new int[] { 1, 0, -1, 0 };

        List<Plot> neighbours = new ArrayList<Plot>();

        for (int i = 0; i < 4; i++) {
            int x = plot.x + dx[i];
            int y = plot.y + dy[i];
            Plot newPlot = new Plot(x, y, plot.getSteps() + 1);
            if (x >= 0 && x < plots[0].length && y >= 0 && y < plots.length && plots[y][x].equals(".")) {
                neighbours.add(newPlot);
                if (newPlot.getSteps() % 2 == 0) {
                    plots[y][x] = "O";
                }
            }
        }
        return neighbours;
    }

    private int countReachable() {
        int count = 0;
        for (String[] row : plots) {
            for (String plot : row) {
                if (plot.equals("O")) {
                    count++;
                }
            }
        }
        return count;
    }

    public int getStartX() {
        return startX;
    }

    public int getStartY() {
        return startY;
    }

    public String toString() {
        String result = "";

        for (String[] row : plots) {
            for (String plot : row) {
                result += plot;
            }
            result += "\n";
        }

        return result;
    }
}
