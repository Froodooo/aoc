package day14;

import java.util.ArrayList;
import java.util.List;

public class Platform {
    private int height;
    private int width;
    List<Rock> rocks;

    public static enum Direction {
        NORTH, SOUTH, EAST, WEST
    }

    public Platform(String input) {
        this.height = input.split("\n").length;
        this.width = input.split("\n")[0].length();
        this.rocks = new ArrayList<Rock>();

        String[] rows = input.split("\n");
        for (int i = 0; i < rows.length; i++) {
            String[] columns = rows[i].split("");
            for (int j = 0; j < columns.length; j++) {
                String type = columns[j];
                if (type.equals(".")) {
                    continue;
                }
                Rock rock = new Rock(type, i, j);
                rocks.add(rock);
            }
        }
    }

    public void tilt(Direction direction) {
        switch (direction) {
            case NORTH:
                tiltNorth();
                break;
            default:
                throw new IllegalArgumentException("Direction not supported");
        }
    }

    public int calculateLoad() {
        int sum = 0;
        for (Rock rock : rocks) {
            if (rock.getType().equals("O")) {
                sum += this.height - rock.getRow();
            }
        }
        return sum;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < this.height; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < this.width; j++) {
                if (hasRock(i, j)) {
                    row.append(getRock(i, j).getType());
                } else {
                    row.append(".");
                }
            }
            sb.append(row.toString() + "\n");
        }
        return sb.toString();
    }

    private void tiltNorth() {
        for (Rock rock : rocks) {
            // System.out.println(rock.toString());
            if (!rock.getType().equals("O")) {
                continue;
            }

            if (rock.getRow() == 0) {
                continue;
            }
            while (!rocks.stream().anyMatch(r -> hasRock(rock.getRow() - 1, rock.getColumn()))) {
                rock.move(Direction.NORTH);
                if (rock.getRow() == 0) {
                    break;
                }
            }
            // System.out.println(rock.toString() + "\n");
        }
    }

    private boolean hasRock(int row, int column) {
        for (Rock rock : rocks) {
            if (rock.getRow() == row && rock.getColumn() == column) {
                return true;
            }
        }
        return false;
    }

    private Rock getRock(int row, int column) {
        for (Rock rock : rocks) {
            if (rock.getRow() == row && rock.getColumn() == column) {
                return rock;
            }
        }
        return null;
    }
}
