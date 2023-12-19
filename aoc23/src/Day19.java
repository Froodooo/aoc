import java.util.ArrayList;
import java.util.List;

import day19.Rating;
import day19.Rule;
import day19.Workflow;

public class Day19 {
    private String input;

    public Day19(String input) {
        this.input = input;

    }

    public int partA() {
        String[] parts = input.split("\n\n");

        List<Workflow> workflows = new ArrayList<>();
        for (String rawWorkflow : parts[0].split("\n")) {
            workflows.add(new Workflow(rawWorkflow));
        }

        List<Rating> ratings = new ArrayList<>();
        for (String rawRating : parts[1].split("\n")) {
            ratings.add(new Rating(rawRating));
        }

        int sum = 0;
        for (Rating rating : ratings) {
            Workflow current = getWorkflow(workflows, "in");
            boolean hasResult = false;
            String result = null;
            while (!hasResult) {
                for (int i = 0; i < current.count(); i++) {
                    Rule rule = current.getRule(i);
                    if (rule.isComparison()) {
                        String categoryLetter = rule.getCategory();
                        int value = rating.getCategory(categoryLetter).getValue();
                        if (rule.isTrue(value)) {
                            if (rule.isResult()) {
                                hasResult = true;
                                result = rule.getResult();
                                break;
                            }

                            current = getWorkflow(workflows, rule.getResult());
                            break;
                        }
                    } else if (rule.isResult()) {
                        hasResult = true;
                        result = rule.getResult();
                        break;
                    } else {
                        current = getWorkflow(workflows, rule.getResult());
                        break;
                    }
                }
            }

            if (result.equals("A")) {
                sum += rating.getScore();
            }
        }

        return sum;
    }

    public int partB() {
        return -1;
    }

    private Workflow getWorkflow(List<Workflow> workflows, String name) {
        for (Workflow workflow : workflows) {
            if (workflow.getName().equals(name)) {
                return workflow;
            }
        }

        return null;
    }
}