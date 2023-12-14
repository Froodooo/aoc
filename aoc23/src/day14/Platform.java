package day14;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Platform {
    private int height;
    private int width;
    List<Rock> rocks;

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

    public void rotate() {
        for (Rock rock : rocks) {
            rock.rotate(width, height);
        }

        int tempHeight = this.height;
        this.height = this.width;
        this.width = tempHeight;
    }

    public void tilt() {
        for (Rock rock : rocks) {
            if (!rock.getType().equals("O")) {
                continue;
            }

            if (rock.getRow() == 0) {
                continue;
            }
            Optional<Rock> blockingCubeRock = rocks.stream()
                    .filter(r -> r.getType().equals("#") && r.getRow() < rock.getRow()
                            && r.getColumn() == rock.getColumn())
                    .min((r1, r2) -> r2.getRow() - r1.getRow());
            long blockingRocks = blockingCubeRock.isPresent() ? rocks.stream()
                    .filter(r -> r.getRow() > blockingCubeRock.get().getRow() && r.getRow() < rock.getRow()
                            && r.getColumn() == rock.getColumn())
                    .count()
                    : rocks.stream()
                            .filter(r -> r.getRow() < rock.getRow() && r.getColumn() == rock.getColumn()).count();

            rock.move(rock.getRow() - (blockingCubeRock.isPresent() ? (blockingCubeRock.get().getRow() + 1) : 0)
                    - blockingRocks);
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

    public void sort() {
        rocks.sort((r1, r2) -> {
            if (r1.getRow() == r2.getRow()) {
                return r1.getColumn() - r2.getColumn();
            }
            return r1.getRow() - r2.getRow();
        });
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
