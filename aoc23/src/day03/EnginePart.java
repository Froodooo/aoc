package day03;

public class EnginePart {
    private String symbol;
    private int row;
    private int index;

    public EnginePart(String symbol, int row, int index) {
        this.symbol = symbol;
        this.row = row;
        this.index = index;
    }

    public int getIndex() {
        return index;
    }

    public int getRow() {
        return row;
    }

    public String getSymbol() {
        return symbol;
    }
}
