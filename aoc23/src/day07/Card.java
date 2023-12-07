package day07;

public class Card implements Comparable<Card> {
    private String value;
    private int strength;

    public Card(String value, boolean joker) {
        this.value = value;
        this.strength = calculateStrength(value, joker);
    }

    private int calculateStrength(String value, boolean joker) {
        switch (value) {
            case "A":
                return 14;
            case "K":
                return 13;
            case "Q":
                return 12;
            case "J":
                return joker ? 1 : 11;
            case "T":
                return 10;
            default:
                return Integer.parseInt(value);
        }
    }

    public int getStrength() {
        return this.strength;
    }

    public String getValue() {
        return this.value;
    }

    public String toString() {
        return value;
    }

    @Override
    public int compareTo(Card o) {
        return this.strength - o.getStrength();
    }
}
