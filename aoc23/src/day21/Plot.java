package day21;

import java.awt.Point;

public class Plot extends Point {
    private int steps;

    public Plot(int x, int y) {
        super(x, y);
        this.steps = 0;
    }

    public Plot(int x, int y, int steps) {
        super(x, y);
        this.steps = steps;
    }

    public int getSteps() {
        return steps;
    }

    public String toString() {
        return String.format("(%d, %d)", x, y);
    }
}
