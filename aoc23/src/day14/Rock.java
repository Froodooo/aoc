package day14;

public class Rock {
    private String type;
    private int row;
    private int column;

    public Rock(String type, int row, int column) {
        this.type = type;
        this.row = row;
        this.column = column;
    }

    public void move(long steps) {
        this.row -= steps;
    }

    public void rotate(int width, int height) {
        int tempRow = this.row;
        this.row = this.column;
        this.column = height - 1 - tempRow;
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
