public class Day13 {
    private String input;
    private boolean currentIsRow = false;
    private boolean currentIsColumn = false;
    private int currentLine = -1;

    public Day13(String input) {
        this.input = input;
    }

    public int partA() {
        int sum = 0;

        for (String pattern : input.split("\n\n")) {
            sum += patternLineValue(pattern);
            currentIsRow = false;
            currentIsColumn = false;
            currentLine = -1;
        }

        return sum;
    }

    public int partB() {
        int sum = 0;
        for (String pattern : input.split("\n\n")) {
            patternLineValue(pattern);
            int lineLength = pattern.split("\n")[0].length();
            String patternLine = pattern.replace("\n", "");
            for (int i = 0; i < patternLine.length(); i++) {
                String replacement = patternLine.charAt(i) == ".".charAt(0) ? "#" : ".";
                String newPattern = patternLine.substring(0, i) + replacement + patternLine.substring(i + 1);
                String[] newPatternArray = newPattern.split("(?<=\\G.{" + lineLength + "})");
                String newPatternWithNewLines = String.join("\n", newPatternArray);
                int value = patternLineValue(newPatternWithNewLines);
                if (value > -1) {
                    sum += value;
                    break;
                }
            }
        }

        return sum;
    }

    private int patternLineValue(String pattern) {
        String[] rows = pattern.split("\n");
        String[] columns = new String[rows[0].length()];
        for (int i = 0; i < rows.length; i++) {
            String row = rows[i];
            for (int j = 0; j < row.length(); j++) {
                if (columns[j] == null) {
                    columns[j] = "";
                }
                columns[j] += row.charAt(j);
            }
        }

        int columnReflection = findColumnReflection(columns);
        int rowReflection = findRowReflection(rows);
        
        if (columnReflection > -1) {
            currentIsColumn = true;
            currentIsRow = false;
            currentLine = columnReflection + 1;
            return columnReflection + 1;
        } else if (rowReflection > -1) {
            currentIsRow = true;
            currentIsColumn = false;
            currentLine = rowReflection + 1;
            return (rowReflection + 1) * 100;
        } else {
            return -1;
        }
    }

    private int findColumnReflection(String[] line) {
        for (int i = 0; i < line.length - 1; i++) {
            String current = line[i];
            String next = line[i + 1];
            if (current.equals(next) && !(currentIsColumn && currentLine == i + 1)) {
                if (canExpandReflection(line, i - 1, i + 2)) {
                    return i;
                }
            }
        }

        return -1;
    }

    private int findRowReflection(String[] line) {
        for (int i = 0; i < line.length - 1; i++) {
            String current = line[i];
            String next = line[i + 1];
            if (current.equals(next) && !(currentIsRow && currentLine == i + 1)) {
                if (canExpandReflection(line, i - 1, i + 2)) {
                    return i;
                }
            }
        }

        return -1;
    }

    private boolean canExpandReflection(String[] line, int left, int right) {
        while (left >= 0 && right < line.length) {
            String current = line[left];
            String next = line[right];
            if (current.equals(next)) {
                left--;
                right++;
            } else {
                return false;
            }
        }

        return true;
    }
}
