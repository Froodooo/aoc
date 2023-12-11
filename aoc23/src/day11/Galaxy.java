package day11;

public class Galaxy {
    private int id;
    private int row;
    private int column;

    public Galaxy(int id, int row, int column) {
        this.id = id;
        this.row = row;
        this.column = column;
    }

    public int getRow() {
        return this.row;
    }

    public int getColumn() {
        return this.column;
    }

    public String toString() {
        return String.format("(%d, %d, %d)", this.id, this.row, this.column);
    }
}
