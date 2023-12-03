package day03;

public class Number {
    private int value;
    private int length;
    private int row;
    private int index;

    public Number(int value, int length, int row, int index) {
        this.value = value;
        this.length = length;
        this.row = row;
        this.index = index;
    }

    public int getIndex() {
        return index;
    }

    public int getLength() {
        return length;
    }

    public int getRow() {
        return row;
    }

    public int getValue() {
        return value;
    }
}
