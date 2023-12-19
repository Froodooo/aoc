package day19;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Workflow {
    String name;
    List<Rule> rules;

    public Workflow(String input) {
        rules = new ArrayList<>();
        Pattern pattern = Pattern.compile("(\\w+)\\{(.*)\\}");
        Matcher matcher = pattern.matcher(input);
        if (matcher.find()) {
            name = matcher.group(1);
            String[] parts = matcher.group(2).split(",");
            for (String part : parts) {
                rules.add(new Rule(part));
            }
        }
    }

    public String getName() {
        return name;
    }

    public Rule getRule(int index) {
        return rules.get(index);
    }

    public Rule getRule(String category) {
        for (Rule rule : rules) {
            if (rule.getCategory().equals(category)) {
                return rule;
            }
        }

        return null;
    }

    public int count() {
        return rules.size();
    }

    public String toString() {
        String result = name + " { ";
        for (Rule rule : rules) {
            result += rule.toString() + " ";
        }
        result += "}";
        return result;
    }
}
