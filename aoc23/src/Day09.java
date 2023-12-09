import day09.Sequence;

public class Day09 {
    private String input;

    public Day09(String input) {
        this.input = input;
    }

    public int partA() {
        int sum = 0;

        for (String line : input.split("\n")) {
            Sequence sequence = new Sequence(line);
            sum += sequence.extrapolate(true);
        }

        return sum;
    }

    public int partB() {
        int sum = 0;

        for (String line : input.split("\n")) {
            Sequence sequence = new Sequence(line);
            sum += sequence.extrapolate(false);
        }

        return sum;
    }
}
