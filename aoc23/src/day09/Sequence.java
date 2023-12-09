package day09;

import java.util.Arrays;

public class Sequence {
    private int[] numbers;

    public Sequence(String line) {
        this.numbers = Arrays.stream(line.split("\\s+")).mapToInt(Integer::parseInt).toArray();
    }

    public int extrapolate(boolean next) {
        return extrapolate(this.numbers, next);
    }

    private int extrapolate(int[] numbers, boolean next) {
        if (Arrays.stream(numbers).allMatch(number -> number == 0)) {
            return 0;
        }

        int[] differences = new int[numbers.length - 1];
        for (int i = 0; i < differences.length; i++) {
            differences[i] = numbers[i + 1] - numbers[i];
        }

        return next ? numbers[numbers.length - 1] + extrapolate(differences, next)
                : numbers[0] - extrapolate(differences, next);
    }
}
