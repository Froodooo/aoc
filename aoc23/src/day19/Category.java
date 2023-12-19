package day19;

public class Category {
    private String name;
    private int value;

    public Category(String input) {
        String[] parts = input.split("=");
        this.name = parts[0].trim();
        this.value = Integer.parseInt(parts[1].trim());
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }

    public String toString() {
        return name + ": " + value;
    }
}
