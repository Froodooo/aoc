import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import day10.Grid;
import day10.Tile;

public class Day10 {
    private String input;

    public Day10(String input) {
        this.input = input;
    }

    public int partA() {
        Grid grid = new Grid(input);
        Tile start = grid.getStart();
        // List<Tile> neighbours = grid.getNeighbours(start);
        // for (Tile neighbour : neighbours) {
        //     System.out.println(neighbour.getX() + ", " + neighbour.getY());
        // }
        List<String> visited = grid.findRoute(start, new ArrayList<String>(Arrays.asList(start.toString())), 0);
        // for (Tile tile : route) {
        //     System.out.println(tile.toString());
        // }

        int furthestPoint = visited.size() / 2;

        return furthestPoint;
    }

    public int partB() {
         Grid grid = new Grid(input);
        Tile start = grid.getStart();
        // List<Tile> neighbours = grid.getNeighbours(start);
        // for (Tile neighbour : neighbours) {
        //     System.out.println(neighbour.getX() + ", " + neighbour.getY());
        // }
        List<String> visited = grid.findRoute(start, new ArrayList<String>(Arrays.asList(start.toString())), 0);
        // for (Tile tile : route) {
        //     System.out.println(tile.toString());
        // }

        int furthestPoint = visited.size() / 2;

        return furthestPoint;
    }
}
