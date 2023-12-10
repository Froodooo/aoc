package day10;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import day10.Tile.Direction;

public class Grid {
    private List<List<Tile>> tiles;
    private Tile start;

    public Grid(String input) {
        tiles = new ArrayList<List<Tile>>();
        String[] rows = input.split("\n");
        for (int y = 0; y < rows.length; y++) {
            List<Tile> row = new ArrayList<Tile>();
            String[] rowTiles = rows[y].split("");
            for (int x = 0; x < rowTiles.length; x++) {
                row.add(new Tile(x, y, rowTiles[x]));
            }
            tiles.add(row);
        }
        start = findStart();
    }

    public Tile getStart() {
        return start;
    }

    public boolean isStart(Tile tile) {
        return tile.getX() == start.getX() && tile.getY() == start.getY();
    }

    public String toString() {
        return tiles.stream().map(row -> row.stream().map(tile -> tile.getType()).collect(Collectors.joining("")))
                .collect(Collectors.joining("\n"));
    }

    public List<String> findRoute(Tile start, List<String> visited, int count) {
        do {
            // System.out.println("Start: " + start.toString());
            List<Tile> neighbours = getNeighbours(start);
            neighbours.removeIf(neighbour -> visited.contains(neighbour.toString()));

            if (neighbours.size() == 0 || visited.contains(neighbours.get(0).toString())) {
                return visited;
            }

            Tile neighbour = neighbours.get(0);
            // System.out.println(neighbours.size());
            // System.out.println("Neighbour: " + neighbours.get(0).toString());

            // System.out.println(visited);
            visited.add(neighbour.toString());
            start = neighbour;
        } while (!start.isStart());

        return visited;
    }

    public List<Tile> getNeighbours(Tile tile) {
        List<Tile> neighbours = new ArrayList<Tile>();
        int x = tile.getX();
        int y = tile.getY();

        // north
        if ((y - 1) >= 0) {
            Tile north = tiles.get(y - 1).get(x);
            if (north.isConnecting(Direction.SOUTH) && tile.isConnecting(Direction.NORTH)) {
                neighbours.add(north);
            }
        }

        // east
        if ((x + 1) < tiles.get(y).size()) {
            Tile east = tiles.get(y).get(x + 1);
            if (east.isConnecting(Direction.WEST) && tile.isConnecting(Direction.EAST)) {
                neighbours.add(east);
            }
        }

        // south
        if ((y + 1) < tiles.size()) {
            Tile south = tiles.get(y + 1).get(x);
            if (south.isConnecting(Direction.NORTH) && tile.isConnecting(Direction.SOUTH)) {
                neighbours.add(south);
            }
        }

        // west
        if ((x - 1) >= 0) {
            Tile west = tiles.get(y).get(x - 1);
            if (west.isConnecting(Direction.EAST) && tile.isConnecting(Direction.WEST)) {
                neighbours.add(west);
            }
        }

        return neighbours;
    }

    private Tile findStart() {
        for (int y = 0; y < tiles.size(); y++) {
            for (int x = 0; x < tiles.get(0).size(); x++) {
                Tile tile = tiles.get(y).get(x);
                if (tile.isStart()) {
                    return tile;
                }
            }
        }

        throw new RuntimeException("No start found");
    }
}
