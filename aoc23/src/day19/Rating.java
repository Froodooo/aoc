package day19;

import java.util.ArrayList;
import java.util.List;

public class Rating {
    List<Category> categories;

    public Rating(String input) {
        categories = new ArrayList<>();
        String[] parts = input.replaceAll("[{}]", "").split(",");
        for (String part : parts) {
            categories.add(new Category(part));
        }
    }

    public Category getCategory(String name) {
        for (Category category : categories) {
            if (category.getName().equals(name)) {
                return category;
            }
        }

        return null;
    }

    public Category getCategory(int index) {
        return categories.get(index);
    }

    public int getScore() {
        int score = 0;

        for (Category category : categories) {
            score += category.getValue();
        }

        return score;
    }

    public String toString() {
        String result = "";
        for (Category category : categories) {
            result += category.toString() + " ";
        }
        return result;
    }
}
