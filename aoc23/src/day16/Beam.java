package day16;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Beam {
    public static enum DIRECTION {
        UP, DOWN, LEFT, RIGHT
    }

    private int x;
    private int y;
    private DIRECTION direction;
    private Set<String> path;
    private List<Beam> splittedBeams;

    public Beam() {
        this.x = 0;
        this.y = 0;
        this.direction = DIRECTION.RIGHT;
        this.path = new HashSet<String>();
        this.splittedBeams = new ArrayList<>();
    }

    public Beam(int x, int y, DIRECTION direction, Set<String> path) {
        this.x = x;
        this.y = y;
        this.direction = direction;
        this.path = path;
        this.splittedBeams = new ArrayList<Beam>();
    }

    public void move(Contraption contraption) {
        if (!contraption.isValidPosition(x, y)) {
            updateSplittedBeamPaths();
            return;
        }
        if (hasVisitedBefore()) {
            updateSplittedBeamPaths();
            return;
        }

        path.add(String.format("%s (%d, %d)", direction.name(), x, y));

        Tile tile = contraption.getTile(x, y);
        if (isHorizontalSplit(tile)) {
            splittedBeams.add(new Beam(x, y, DIRECTION.RIGHT, path));
        } else if (isVerticalSplit(tile)) {
            splittedBeams.add(new Beam(x, y, DIRECTION.DOWN, path));            
        }

        updateDirection(tile);
        updatePosition(contraption);

        move(contraption);
    }

    public Set<String> getPath() {
        return path;
    }

    public List<Beam> getSplittedBeams() {
        return splittedBeams;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public DIRECTION getDirection() {
        return direction;
    }

    private boolean hasVisitedBefore() {
        return path.stream().filter(p -> p.equals(String.format("%s (%d, %d)", direction.name(), x, y))).count() > 0;
    }

    private boolean isHorizontalSplit(Tile tile) {
        return tile.getType() == Tile.Type.HORIZONTAL_SPLITTER;
    }

    private boolean isVerticalSplit(Tile tile) {
        return tile.getType() == Tile.Type.VERTICAL_SPLITTER;
    }

    private void updateSplittedBeamPaths() {
        for (Beam beam : splittedBeams) {
            beam.setPath(path);
        }
    }

    private void setPath(Set<String> path) {
        this.path = path;
    }

    private void updateDirection(Tile tile) {
        switch (tile.getType()) {
            case FORWARD_MIRROR:
                switch (direction) {
                    case UP:
                        direction = DIRECTION.RIGHT;
                        break;
                    case DOWN:
                        direction = DIRECTION.LEFT;
                        break;
                    case LEFT:
                        direction = DIRECTION.DOWN;
                        break;
                    case RIGHT:
                        direction = DIRECTION.UP;
                        break;
                }
                break;
            case BACKWARD_MIRROR:
                switch (direction) {
                    case UP:
                        direction = DIRECTION.LEFT;
                        break;
                    case DOWN:
                        direction = DIRECTION.RIGHT;
                        break;
                    case LEFT:
                        direction = DIRECTION.UP;
                        break;
                    case RIGHT:
                        direction = DIRECTION.DOWN;
                        break;
                }
                break;
            case HORIZONTAL_SPLITTER:
                switch (direction) {
                    case UP:
                        direction = DIRECTION.LEFT;
                        break;
                    case DOWN:
                        direction = DIRECTION.LEFT;
                        break;
                    default:
                        break;
                }
                break;
            case VERTICAL_SPLITTER:
                switch (direction) {
                    case LEFT:
                        direction = DIRECTION.UP;
                        break;
                    case RIGHT:
                        direction = DIRECTION.UP;
                        break;
                    default:
                        break;
                }
                break;
            default:
                break;
        }
    }

    private void updatePosition(Contraption contraption) {
        switch (direction) {
            case UP:
                y--;
                break;
            case DOWN:
                y++;
                break;
            case LEFT:
                x--;
                break;
            case RIGHT:
                x++;
                break;
        }
    }
}
