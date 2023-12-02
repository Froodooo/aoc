package day02;

public class Record {
    private int red;
    private int blue;
    private int green;

    public Record(int red, int green, int blue) {
        this.red = red;
        this.green = green;
        this.blue = blue;
    }

    public int getRed() {
        return red;
    }

    public int getBlue() {
        return blue;
    }

    public int getGreen() {
        return green;
    }

    public String toString() {
        return red + " " + green + " " + blue;
    }
}
