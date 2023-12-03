import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import day03.EnginePart;
import day03.Number;

public class Day03 {
    private String input;

    public Day03(String input) {
        this.input = input;
    }

    public int partA() {
        String[] engineRows = input.split("\n");

        List<Number> numbers = findNumbers(engineRows);
        int sum = calculateSum(numbers, engineRows);

        return sum;
    }

    public int partB() {
        String[] engineRows = input.split("\n");

        List<Number> numbers = findNumbers(engineRows);
        List<EnginePart> engineParts = findEngineParts(engineRows).stream().filter(part -> part.getSymbol().equals("*"))
                .toList();

        int sum = calculateProduct(numbers, engineParts);

        return sum;
    }

    private List<Number> findNumbers(String[] engineRows) {
        List<Number> numbers = new ArrayList<Number>();
        for (int i = 0; i < engineRows.length; i++) {
            Pattern pattern = Pattern.compile("\\d+");
            Matcher matcher = pattern.matcher(engineRows[i]);

            while (matcher.find()) {
                Number number = new Number(Integer.parseInt(matcher.group()), matcher.group().length(), i,
                        matcher.start());
                numbers.add(number);
            }
        }

        return numbers;
    }

    private List<EnginePart> findEngineParts(String[] engineRows) {
        List<EnginePart> engineParts = new ArrayList<EnginePart>();
        for (int i = 0; i < engineRows.length; i++) {
            for (int j = 0; j < engineRows[i].length(); j++) {
                String character = String.valueOf(engineRows[i].charAt(j));
                if (isEnginePart(character)) {
                    EnginePart enginePart = new EnginePart(character, i, j);
                    engineParts.add(enginePart);
                }
            }
        }

        return engineParts;
    }

    private int calculateSum(List<Number> numbers, String[] engineRows) {
        int sum = 0;
        for (Number number : numbers) {
            boolean enginePartFound = false;
            for (int k = -1; k <= 1; k++) {
                for (int l = -1; l <= number.getLength(); l++) {
                    int y = number.getRow() + k;
                    int x = number.getIndex() + l;
                    if (y >= 0 && y < engineRows.length && x >= 0 && x < engineRows[y].length()) {
                        String character = String.valueOf(engineRows[y].charAt(x));
                        if (isEnginePart(character)) {
                            enginePartFound = true;
                            sum += number.getValue();
                            break;
                        }
                    }
                }
                if (enginePartFound) {
                    break;
                }
            }
        }

        return sum;
    }

    private int calculateProduct(List<Number> numbers, List<EnginePart> engineParts) {
        int sum = 0;

        for (EnginePart enginePart : engineParts) {
            int[] rowRange = new int[] { enginePart.getRow() - 1, enginePart.getRow(), enginePart.getRow() + 1 };
            int[] indexRange = new int[] { enginePart.getIndex() - 1, enginePart.getIndex(),
                    enginePart.getIndex() + 1 };
            List<Number> numbersInRange = new ArrayList<Number>();
            for (Number number : numbers) {
                if (IntStream.of(rowRange).anyMatch(x -> x == number.getRow())
                        && (IntStream.of(indexRange).anyMatch(x -> x == number.getIndex())
                                || (IntStream.of(indexRange)
                                        .anyMatch(x -> x == number.getIndex() + number.getLength() - 1)))) {
                    numbersInRange.add(number);
                }
            }

            if (numbersInRange.size() == 2) {
                sum += (numbersInRange.get(0).getValue() * numbersInRange.get(1).getValue());
            }
        }

        return sum;
    }

    private boolean isEnginePart(String character) {
        return !Character.isDigit(character.charAt(0)) && !character.equals(".");
    }
}
