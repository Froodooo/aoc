package aoc23;

public class Day01 {
    private static final String[] WRITTEN_NUMBERS = { "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine" };

    private String input;

    public Day01(String input) {
        this.input = input;
    }

    public void partA() {
        String[] calibrationValues = Utils.separateValues(input, "\n");

        int sum = 0;
        for (String value : calibrationValues) {
            String[] numberValues = value.replaceAll("\\D+", "").split("");
            String firstNumber = numberValues[0];
            String lastNumber = numberValues[numberValues.length - 1];
            int number = Integer.parseInt(firstNumber + lastNumber);
            sum += number;
        }

        System.out.println(sum);
    }

    public void partB() {
        String[] calibrationValues = Utils.separateValues(input, "\n");

        int sum = 0;
        for (String value : calibrationValues) {
            value = replaceLastString(replaceFirstString(value));
            String[] numberValues = value.replaceAll("\\D+", "").split("");
            String firstNumber = numberValues[0];
            String lastNumber = numberValues[numberValues.length - 1];
            int number = Integer.parseInt(firstNumber + lastNumber);
            sum += number;
        }

        System.out.println(sum);
    }

    private String replaceFirstString(String value) {
        int lowestIndex = Integer.MAX_VALUE;
        String firstNumber = "";
        int replacementNumber = 0;
        for (int i = 0; i < WRITTEN_NUMBERS.length; i++) {
            int index = value.indexOf(WRITTEN_NUMBERS[i]);
            if (index != -1 && index < lowestIndex) {
                lowestIndex = index;
                firstNumber = WRITTEN_NUMBERS[i];
                replacementNumber = i + 1;
            }
        }

        if (firstNumber != "") {
            value = value.replace(firstNumber, Integer.toString(replacementNumber));
        }

        return value;
    }

    private String replaceLastString(String value) {
        int highestIndex = Integer.MIN_VALUE;
        String lastNumber = "";
        int replacementNumber = 0;
        for (int i = 0; i < WRITTEN_NUMBERS.length; i++) {
            int index = value.lastIndexOf(WRITTEN_NUMBERS[i]);
            if (index != -1 && index > highestIndex) {
                highestIndex = index;
                lastNumber = WRITTEN_NUMBERS[i];
                replacementNumber = i + 1;
            }
        }

        if (lastNumber != "") {
            value = value.replace(lastNumber, Integer.toString(replacementNumber));
        }

        return value;
    }
}