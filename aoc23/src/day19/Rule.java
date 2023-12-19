package day19;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Rule {
    public static enum Operation { LESS_THAN, GREATER_THAN };
    
    boolean isComparison;

    String category;
    Operation operation;
    int value;
    String result;

    public Rule(String input) {
        Pattern pattern = Pattern.compile("([x|m|a|s])([<>])(\\d+):(\\w+)");
        Matcher matcher = pattern.matcher(input);
        if (matcher.find()) {
            isComparison = true;
            category = matcher.group(1);
            operation = getOperation(matcher.group(2));
            value = Integer.parseInt(matcher.group(3));
            result = matcher.group(4);
        } else {
            isComparison = false;
            result = input;
        }
    }

    public boolean isTrue(int input) {
        if (isComparison) {
            switch (operation) {
                case LESS_THAN:
                    return input < value;
                case GREATER_THAN:
                    return input > value;
                default:
                    return false;
            }
        } else {
            return true;
        }
    }

    public String getCategory() {
        return category;
    }

    public String getResult() {
        return result;
    }

    public boolean isComparison() {
        return isComparison;
    }

    public boolean isResult() {
        return result.equals("A") || result.equals("R");
    }

    private Operation getOperation(String input) {
        if (input.equals("<")) {
            return Operation.LESS_THAN;
        } else if (input.equals(">")) {
            return Operation.GREATER_THAN;
        } else {
            return null;
        }
    }

    public String toString() {
        return isComparison ? category + operation + value + result : result;
    }
}
