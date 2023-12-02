package day02;

import java.util.ArrayList;
import java.util.List;

public class Game {
    private int id;
    private List<Record> records;

    public Game(int id) {
        this.id = id;
        this.records = new ArrayList<Record>();
    }

    public int getId() {
        return id;
    }

    public void addRecord(int red, int green, int blue) {
        this.records.add(new Record(red, green, blue));
    }

    public int getMax(String color) {
        int max = 0;
        for (Record record : records) {
            switch (color) {
                case "red":
                    if (record.getRed() > max) {
                        max = record.getRed();
                    }
                    break;
                case "green":
                    if (record.getGreen() > max) {
                        max = record.getGreen();
                    }
                    break;
                case "blue":
                    if (record.getBlue() > max) {
                        max = record.getBlue();
                    }
                    break;
                default:
                    break;
            }
        }

        return max;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append("Game " + id + "\n");

        for (Record record : records) {
            sb.append(record.toString() + "\n");
        }

        return sb.toString();
    }
}
