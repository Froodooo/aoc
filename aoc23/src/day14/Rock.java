package day14;

import day14.Platform.Direction;

public class Rock {
    private String type;
    private int row;
    private int column;

    public Rock(String type, int row, int column) {
        this.type = type;
        this.row = row;
        this.column = column;
    }

    public void move(Direction direction) {
        switch (direction) {
            case Direction.NORTH:
                this.row--;
                break;
            default:
                throw new IllegalArgumentException("Direction not supported");
        }
    }

    public String getType() {
        return type;
    }

    public int getRow() {
        return row;
    }

    public int getColumn() {
        return column;
    }

    public String toString() {
        return String.format("%s(%d, %d)", type, row, column);
    }
}
