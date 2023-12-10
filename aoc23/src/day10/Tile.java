package day10;

import java.util.Arrays;
import java.util.HashSet;

public class Tile {
    public enum Direction {
        NORTH, EAST, SOUTH, WEST
    }

    private static String NORTH_SOUTH = "|";
    private static String EAST_WEST = "-";
    private static String NORTH_EAST = "L";
    private static String NORTH_WEST = "J";
    private static String SOUTH_WEST = "7";
    private static String SOUTH_EAST = "F";

    private int x;
    private int y;
    private String type;
    private Direction[] connecting;

    public Tile(int x, int y, String type) {
        this.x = x;
        this.y = y;
        this.type = type;
        this.connecting = setConnecting();
    }

    public boolean isStart() {
        return type.equals("S");
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String getType() {
        return type;
    }

    public Direction[] getConnecting() {
        return connecting;
    }

    public boolean isConnecting(Tile tile) {
        return Arrays.stream(this.connecting).filter(d -> Arrays.stream(tile.getConnecting()).anyMatch(c -> c == d)).count() > 0;
    }

    public boolean isConnecting(Direction direction) {
        return Arrays.stream(this.connecting).anyMatch(d -> d == direction);
    }

    private Direction[] setConnecting() {
        switch (this.type) {
            case "|":
                return new Direction[] { Direction.NORTH, Direction.SOUTH };
            case "-":
                return new Direction[] { Direction.EAST, Direction.WEST };
            case "L":
                return new Direction[] { Direction.NORTH, Direction.EAST };
            case "J":
                return new Direction[] { Direction.NORTH, Direction.WEST };
            case "7":
                return new Direction[] { Direction.SOUTH, Direction.WEST };
            case "F":
                return new Direction[] { Direction.SOUTH, Direction.EAST };
            case "S":
                return new Direction[] { Direction.EAST, Direction.SOUTH };
            default:
                return new Direction[] {};
        }
    }

    public String toString() {
        return String.format("(%d, %d, %s)", x, y, type);
    }

    public boolean equals(Object obj) {
        final Tile other = (Tile) obj;
        return this.x == other.x && this.y == other.y;
    }
}
