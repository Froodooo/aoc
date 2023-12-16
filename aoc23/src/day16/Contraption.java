package day16;

import java.util.ArrayList;
import java.util.List;

public class Contraption {
    private List<Tile> tiles;
    private int width;
    private int height;

    public Contraption(String input) {
        tiles = new ArrayList<>();

        String[] lines = input.split("\n");
        this.width = lines[0].length();
        this.height = lines.length;

        for (int y = 0; y < lines.length; y++) {
            String[] chars = lines[y].split("");
            for (int x = 0; x < chars.length; x++) {
                tiles.add(new Tile(chars[x], x, y));
            }
        }
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public Tile getTile(int x, int y) {
        return tiles.stream().filter(tile -> tile.getX() == x && tile.getY() == y).findFirst().orElse(null);
    }

    public boolean isValidPosition(int x, int y) {
        return x >= 0 && x < width && y >= 0 && y < height;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int y = 0; y < height; y++) {
            sb.append("\n");
            for (int x = 0; x < width; x++) {
                Tile tile = getTile(x, y);
                sb.append(tile.getRawType());
            }
        }
        return sb.toString();
    }
}
