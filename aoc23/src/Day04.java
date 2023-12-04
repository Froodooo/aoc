import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import day04.Card;

public class Day04 {
    private String input;

    public Day04(String input) {
        this.input = input;
    }

    public int partA() {
        List<Card> cards = parseCards(input);

        int sum = 0;
        for (Card card : cards) {
            sum += card.getPoints();
        }

        return sum;
    }

    public int partB() {
        List<Card> cards = parseCards(input);

        HashMap<Integer, Integer> allCards = new HashMap<Integer, Integer>();
        for (int i = 1; i <= cards.size(); i++) {
            allCards.put(i, 1);
        }

        for (Card card : cards) {
            int id = card.getId();
            int copiesWon = card.getMatches().length;
            int totalCards = allCards.get(id);
            for (int i = 0; i < totalCards; i++) {
                for (int j = id + 1; j <= id + copiesWon; j++) {
                    allCards.put(j, allCards.get(j) + 1);
                }
            }
        }

        int sum = 0;
        for (int i = 1; i <= allCards.size(); i++) {
            sum += allCards.get(i);
        }

        return sum;
    }

    private List<Card> parseCards(String input) {
        String[] lines = input.split("\n");
        List<Card> cards = new ArrayList<Card>();

        for (int i = 0; i < lines.length; i++) {
            String[] tokens = lines[i].split(":");
            int id = Integer.parseInt(tokens[0].split("\\s+")[1]);
            String[] numbers = tokens[1].split("\\|");
            int[] yourNumbers = Arrays.stream(numbers[0].trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int[] winningNumbers = Arrays.stream(numbers[1].trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            cards.add(new Card(id, yourNumbers, winningNumbers));
        }

        return cards;
    }
}
