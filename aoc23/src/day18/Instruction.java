package day18;

public class Instruction {
    public static enum Direction {
        UP, DOWN, LEFT, RIGHT
    }

    private Direction direction;
    private int meters;

    public Instruction(String instruction, boolean isHex) {
        String[] parts = instruction.split(" ");
        if (isHex) {
            String color = parts[2].replaceAll("[()#]", "");
            this.direction = getDirection(color.substring(5));
            this.meters = getMeters(color.substring(0, 5));
        } else {
            this.direction = getDirection(parts[0]);
            this.meters = Integer.parseInt(parts[1]);
        }
    }

    private int getMeters(String hexMeters) {
        return Integer.parseInt(hexMeters, 16);
    }

    private Direction getDirection(String rawDirection) {
        switch (rawDirection) {
            case "U":
            case "3":
                return Direction.UP;
            case "D":
            case "1":
                return Direction.DOWN;
            case "L":
            case "2":
                return Direction.LEFT;
            case "R":
            case "0":
                return Direction.RIGHT;
            default:
                throw new IllegalArgumentException("Invalid direction: " + rawDirection);
        }
    }

    public Direction getDirection() {
        return direction;
    }

    public int getMeters() {
        return meters;
    }
}
