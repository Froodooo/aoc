package day23;

import java.awt.Point;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

import day23.Tile.Direction;

public class Trail {
    String[][] path;

    Tile entry;
    Tile exit;

    public Trail(String input) {
        String[] lines = input.split("\n");

        path = new String[lines.length][];
        for (int i = 0; i < lines.length; i++) {
            path[i] = lines[i].split("");
            if (i == 0) {
                for (int j = 0; j < path[i].length; j++) {
                    if (path[i][j].equals(".")) {
                        entry = new Tile(j, i);
                    }
                }
            }
            if (i == lines.length - 1) {
                for (int j = 0; j < path[i].length; j++) {
                    if (path[i][j].equals(".")) {
                        exit = new Tile(j, i);
                    }
                }
            }
        }
    }

    public int walk() {
        Queue<Tile> queue = new ArrayDeque<Tile>();

        entry.addVisited(entry.getX() + "," + entry.getY());
        queue.add(entry);

        int maxDistance = 0;

        while (!queue.isEmpty()) {
            Tile current = queue.poll();
            // System.out.println(current.toString());

            if (current.toString().equals(exit.toString())) {
                if (current.getDistance() > maxDistance) {
                    maxDistance = current.getDistance();
                }
            }

            List<Tile> neighbours = neighbours(current);
            queue.addAll(neighbours);
        }

        return maxDistance;
    }

    private List<Tile> neighbours(Tile tile) {
        List<Tile> neighbours = new ArrayList<Tile>();

        int[] dx = { 0, 0, -1, 1 };
        int[] dy = { -1, 1, 0, 0 };
        Direction[] directions = { Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT };

        for (int i = 0; i < dx.length; i++) {
            int x = (int) tile.getX() + dx[i];
            int y = (int) tile.getY() + dy[i];

            if (x >= 0 && x < path[0].length && y >= 0 && y < path.length && !path[y][x].equals("#")
                    && !tile.getVisited().contains(x + "," + y)) {
                if (isDownhill(tile, directions[i])) {
                    Tile newTile = new Tile(x, y, directions[i], path[y][x], tile.getVisited());
                    newTile.addVisited(x + "," + y);
                    neighbours.add(newTile);
                }
            }
        }

        return neighbours;
    }

    private boolean isDownhill(Tile tile, Direction direction) {
        if (tile.getType().equals(".")) {
            return true;
        } else if (tile.getType().equals(">") && direction == Direction.RIGHT) {
            return true;
        } else if (tile.getType().equals("<") && direction == Direction.LEFT) {
            return true;
        } else if (tile.getType().equals("^") && direction == Direction.UP) {
            return true;
        } else if (tile.getType().equals("v") && direction == Direction.DOWN) {
            return true;
        } else {
            return false;
        }
    }

    public Point getEntry() {
        return entry;
    }

    public Point getExit() {
        return exit;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (String[] row : path) {
            for (String cell : row) {
                sb.append(cell);
            }
            sb.append("\n");
        }
        return sb.toString();
    }
}
