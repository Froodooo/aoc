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
        List<String> visited = grid.findRoute(start, new ArrayList<String>(Arrays.asList(start.toString())), 0);

        int furthestPoint = visited.size() / 2;

        return furthestPoint;
    }

    public int partB() {
        Grid grid = new Grid(input, true);
        Tile start = grid.getStart();
        List<String> visited = grid.findRoute(start, new ArrayList<String>(Arrays.asList(start.toString())), 0);

        int inside = grid.insideTiles(visited);

        return inside;
    }
}
