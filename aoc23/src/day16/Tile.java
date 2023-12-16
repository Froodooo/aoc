package day16;

public class Tile {
    public static enum Type {
        EMPTY, FORWARD_MIRROR, BACKWARD_MIRROR, HORIZONTAL_SPLITTER, VERTICAL_SPLITTER
    }

    private String rawType;
    private Type type;
    private int x;
    private int y;

    public Tile(String type, int x, int y) {
        switch (type) {
            case ".":
                this.type = Type.EMPTY;
                break;
            case "/":
                this.type = Type.FORWARD_MIRROR;
                break;
            case "\\":
                this.type = Type.BACKWARD_MIRROR;
                break;
            case "-":
                this.type = Type.HORIZONTAL_SPLITTER;
                break;
            case "|":
                this.type = Type.VERTICAL_SPLITTER;
                break;
            default:
                throw new IllegalArgumentException("Invalid type: " + type);
        }

        this.rawType = type;
        this.x = x;
        this.y = y;
    }

    public Type getType() {
        return type;
    }

    public String getRawType() {
        return rawType;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String toString() {
        return String.format("%s (%d, %d)", type, x, y);
    }
}
