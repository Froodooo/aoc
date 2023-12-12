import java.util.Arrays;

public class Day12 {
    private String input;

    public Day12(String input) {
        this.input = input;
    }

    public int partA() {
        int sum = 0;
        for (String line : input.split("\n")) {
            int lineSum = lineSum(line);
            sum += lineSum;
        }
        return sum;
    }

    public int partB() {
        return -1;
    }

    private int lineSum(String line) {
        String records = line.split(" ")[0];
        int[] groups = Arrays.stream(line.split(" ")[1].split(","))
                .mapToInt(Integer::parseInt)
                .toArray();

        int totalQuestionMarks = Arrays.stream(records.split("")).filter(s -> s.equals("?")).toArray().length;
        int totalHashes = Arrays.stream(records.split("")).filter(s -> s.equals("#")).toArray().length;
        int minQuestionMarks = Arrays.stream(groups).sum() - totalHashes;

        int lineSum = 0;
        for (int i = minQuestionMarks; i < Math.pow(2, totalQuestionMarks); i++) {
            String binary = getBinary(i, totalQuestionMarks);
            int[] groupsToCompare = groupsToCompare(records, totalQuestionMarks, binary);
            if (Arrays.equals(groups, groupsToCompare)) {
                lineSum++;
            }
        }
        return lineSum;
    }

    private String getBinary(int number, int totalQuestionMarks) {
        String binary = Integer.toBinaryString(number);
        while (binary.length() < totalQuestionMarks) {
            binary = "0" + binary;
        }
        return binary;
    }

    private int[] groupsToCompare(String records, int totalQuestionMarks, String binary) {

        int[] binaryArray = Arrays.stream(binary.split(""))
                .mapToInt(Integer::parseInt)
                .toArray();

        int binaryCount = 0;
        String recordsCopy = records;
        for (int j = 0; j < records.length(); j++) {
            if (records.charAt(j) == '?') {
                recordsCopy = recordsCopy.substring(0, j) + getSpring(binaryArray[binaryCount])
                        + records.substring(j + 1);
                binaryCount++;
            }
        }
        int[] groupsToCompare = Arrays.stream(recordsCopy.split("\\.+")).mapToInt(String::length).toArray();
        if (recordsCopy.startsWith(".") && groupsToCompare.length > 0) {
            groupsToCompare = Arrays.copyOfRange(groupsToCompare, 1, groupsToCompare.length);
        }
        return groupsToCompare;
    }

    private String getSpring(int number) {
        return number == 0 ? "." : "#";
    }
}
