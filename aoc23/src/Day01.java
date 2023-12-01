public class Day01 {
    private static final String[] WRITTEN_NUMBERS = { "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine" };

    private String input;

    public Day01(String input) {
        this.input = input;
    }

    public int partA() {
        String[] calibrationValues = Utils.separateValues(input, "\n");

        int sum = 0;
        for (String value : calibrationValues) {
            String[] numberValues = value.replaceAll("\\D+", "").split("");
            String firstNumber = numberValues[0];
            String lastNumber = numberValues[numberValues.length - 1];
            int number = Integer.parseInt(firstNumber + lastNumber);
            sum += number;
        }

        return sum;
    }

    public int partB() {
        String[] calibrationValues = Utils.separateValues(input, "\n");

        int sum = 0;
        for (String value : calibrationValues) {
            value = replaceWrittenNumbers(value);
            String[] numberValues = value.replaceAll("\\D+", "").split("");
            String firstNumber = numberValues[0];
            String lastNumber = numberValues[numberValues.length - 1];
            int number = Integer.parseInt(firstNumber + lastNumber);
            sum += number;
        }

        return sum;
    }

    private String replaceWrittenNumbers(String value) {
        int lowestIndex = Integer.MAX_VALUE;
        int highestIndex = Integer.MIN_VALUE;
        String firstNumber = "";
        String lastNumber = "";
        int firstReplacement = 0;
        int lastReplacement = 0;

        for (int i = 0; i < WRITTEN_NUMBERS.length; i++) {
            int firstIndex = value.indexOf(WRITTEN_NUMBERS[i]);
            if (firstIndex != -1 && firstIndex < lowestIndex) {
                lowestIndex = firstIndex;
                firstNumber = WRITTEN_NUMBERS[i];
                firstReplacement = i + 1;
            }

            int lastIndex = value.lastIndexOf(WRITTEN_NUMBERS[i]);
            if (lastIndex != -1 && lastIndex > highestIndex) {
                highestIndex = lastIndex;
                lastNumber = WRITTEN_NUMBERS[i];
                lastReplacement = i + 1;
            }
        }

        if (firstNumber != "") {
            value = value.replace(firstNumber, Integer.toString(firstReplacement));
        }

        if (lastNumber != "") {
            value = value.replace(lastNumber, Integer.toString(lastReplacement));
        }

        return value;
    }
}