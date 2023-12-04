package day04;

import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public class Card {
    private int id;
    private int[] numbers;
    private int[] winningNumbers;

    public Card(int id, int[] numbers, int[] winningNumbers) {
        this.id = id;
        this.numbers = numbers;
        this.winningNumbers = winningNumbers;
    }

    public int getId() {
        return id;
    }

    public int[] getNumbers() {
        return numbers;
    }

    public int[] getWinningNumbers() {
        return winningNumbers;
    }

    public int getPoints() {
        return (int) Math.pow(2, getMatches().length - 1);
    }

    public int[] getMatches() {
        Set<Integer> numbersSet = Arrays.stream(numbers).boxed().collect(Collectors.toSet());
        Set<Integer> winningNumbersSet = Arrays.stream(winningNumbers).boxed().collect(Collectors.toSet());

        numbersSet.retainAll(winningNumbersSet);

        return Arrays.stream(numbersSet.toArray(new Integer[numbersSet.size()])).mapToInt(Integer::intValue).toArray();
    }

    public String toString() {
        return String.format("Card %d: %s | %s", id, Arrays.toString(numbers), Arrays.toString(winningNumbers));
    }
}
