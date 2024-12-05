package day23;

import java.awt.Point;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Tile extends Point {
    public enum Direction {
        UP, DOWN, LEFT, RIGHT
    }

    private Direction direction;
    private String type;
    private Set<String> visited;

    public Tile(int x, int y) {
        super(x, y);
        this.direction = Direction.DOWN;
        this.type = ".";
        this.visited = new HashSet<String>();
    }

    public Tile(int x, int y, Direction direction, String type, Set<String> visited) {
        super(x, y);
        this.direction = direction;
        this.type = type;
        this.visited = visited;
    }

    public void setVisited(Set<String> visited) {
        this.visited = visited;
    }

    public void addVisited(String key) {
        visited.add(key);
    }

    public int getDistance() {
        return visited.size();
    }

    public Direction getDirection() {
        return direction;
    }

    public String getType() {
        return type;
    }

    public Set<String> getVisited() {
        return visited;
    }
}
