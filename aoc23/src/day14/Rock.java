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

    public void move(Direction direction, long steps) {
        switch (direction) {
            case Direction.NORTH:
                this.row -= steps;
                break;
            default:
                throw new IllegalArgumentException("Direction not supported");
        }
    }

    public void rotate(Direction direction, int width, int height) {
        switch (direction) {
            case Direction.WEST:
                int tempRow = this.row;
                this.row = this.column;
                this.column = height - 1 - tempRow;
                break;
            case Direction.SOUTH:
                this.row = height - 1 - this.row;
                this.column = width - 1 - this.column;
                break;
            case Direction.EAST:
                tempRow = this.row;
                this.row = width - 1 - this.column;
                this.column = tempRow;
                break;
            case Direction.NORTH:
                throw new IllegalArgumentException("Direction not supported");
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
