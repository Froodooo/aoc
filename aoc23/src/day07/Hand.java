package day07;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

public class Hand implements Comparable<Hand> {
    private List<Card> cards;
    private List<Card> jokers;
    private int bid;
    private int score;

    public Hand(String allCards, int bid, boolean joker) {
        this.cards = new ArrayList<Card>();
        this.jokers = new ArrayList<Card>();
        String[] cardStrings = allCards.split("");
        for (int i = 0; i < cardStrings.length; i++) {
            this.cards.add(new Card(cardStrings[i], joker));
            this.jokers.add(new Card(cardStrings[i], joker));
        }

        this.bid = bid;
        this.score = calculateScore(false);
        if (joker) {
            int numberOfJokers = Arrays.stream(cardStrings).filter(c -> c.equals("J")).toArray().length;
            assignJokers(numberOfJokers);
            this.score = calculateScore(joker);
        }
    }

    private void assignJokers(int numberOfJokers) {
        if (numberOfJokers == 5) {
            this.jokers = Arrays.asList(new Card("A", true), new Card("A", true), new Card("A", true), new Card("A", true), new Card("A", true));
            return;
        }

        if (numberOfJokers == 0) {
            return;
        }

        String highestNonJoker = this.jokers.stream().filter(c -> !c.getValue().equals("J"))
                .sorted((c1, c2) -> {
                    return c2.getStrength() - c1.getStrength();
                }).findFirst().orElse(null).getValue();

        switch (this.score) {
            case 6:
            case 5:
                for (int i = 0; i < this.jokers.size(); i++) {
                    if (this.jokers.get(i).getValue().equals("J")) {
                        this.jokers.set(i, new Card(highestNonJoker, true));
                    }
                }
                break;
            case 4:
                if (numberOfJokers == 3) {
                    for (int i = 0; i < this.jokers.size(); i++) {
                        if (this.jokers.get(i).getValue().equals("J")) {
                            this.jokers.set(i, new Card(highestNonJoker, true));
                        }
                    }
                } else {
                    Map<String, Integer> cardCount = new HashMap<String, Integer>();
                    for (String card : getCards(true)) {
                        if (cardCount.containsKey(card)) {
                            cardCount.put(card, cardCount.get(card) + 1);
                        } else {
                            cardCount.put(card, 1);
                        }
                    }
                    String threeOfAKind = cardCount.entrySet().stream().filter(e -> e.getValue() == 3).findFirst()
                            .orElse(null).getKey();
                    for (int i = 0; i < this.jokers.size(); i++) {
                        if (this.jokers.get(i).getValue().equals("J")) {
                            this.jokers.set(i, new Card(threeOfAKind, true));
                        }
                    }
                }
                break;
            case 3:
                if (numberOfJokers == 2) {
                    Map<String, Integer> cardCount = new HashMap<String, Integer>();
                    for (String card : getCards(true)) {
                        if (cardCount.containsKey(card)) {
                            cardCount.put(card, cardCount.get(card) + 1);
                        } else {
                            cardCount.put(card, 1);
                        }
                    }
                    String nonJokerPair = cardCount.entrySet().stream()
                            .filter(e -> e.getValue() == 2 && !e.getKey().equals("J")).findFirst().orElse(null)
                            .getKey();
                    for (int i = 0; i < this.jokers.size(); i++) {
                        if (this.jokers.get(i).getValue().equals("J")) {
                            this.jokers.set(i, new Card(nonJokerPair, true));
                        }
                    }
                } else {
                    for (int i = 0; i < this.jokers.size(); i++) {
                        if (this.jokers.get(i).getValue().equals("J")) {
                            this.jokers.set(i, new Card(highestNonJoker, true));
                        }
                    }
                }
                break;
            case 2:
                if (numberOfJokers == 2) {
                    for (int i = 0; i < this.jokers.size(); i++) {
                        if (this.jokers.get(i).getValue().equals("J")) {
                            this.jokers.set(i, new Card(highestNonJoker, true));
                        }
                    }
                } else {
                    Map<String, Integer> cardCount = new HashMap<String, Integer>();
                    for (String card : getCards(true)) {
                        if (cardCount.containsKey(card)) {
                            cardCount.put(card, cardCount.get(card) + 1);
                        } else {
                            cardCount.put(card, 1);
                        }
                    }
                    String nonJokerPair = cardCount.entrySet().stream()
                            .filter(e -> e.getValue() == 2 && !e.getKey().equals("J")).findFirst().orElse(null)
                            .getKey();
                    for (int i = 0; i < this.jokers.size(); i++) {
                        if (this.jokers.get(i).getValue().equals("J")) {
                            this.jokers.set(i, new Card(nonJokerPair, true));
                        }
                    }
                }
                break;
            case 1:
                for (int i = 0; i < this.jokers.size(); i++) {
                    if (this.jokers.get(i).getValue().equals("J")) {
                        this.jokers.set(i, new Card(highestNonJoker, true));
                    }
                }
                break;
        }
    }

    public int getScore() {
        return this.score;
    }

    public int getBid() {
        return this.bid;
    }

    public List<String> getCards(boolean joker) {
        List<String> cardStrings = new ArrayList<String>();
        if (joker) {
            for (int i = 0; i < jokers.size(); i++) {
                cardStrings.add(jokers.get(i).toString());
            }
        } else {
            for (int i = 0; i < this.cards.size(); i++) {
                cardStrings.add(this.cards.get(i).toString());
            }
        }

        return cardStrings;
    }



    public String toString() {
        StringBuilder cardString = new StringBuilder();
        for (Card card : this.jokers) {
            cardString.append(card.toString());
        }

        return String.format("%s %d %d", cardString.toString(), bid, score);
    }

    private int calculateScore(boolean joker) {
        int score = 0;

        if (isFiveOfAKind(joker)) {
            score = 7;
        } else if (isFourOfAKind(joker)) {
            score = 6;
        } else if (isFullHouse(joker)) {
            score = 5;
        } else if (isThreeOfAKind(joker)) {
            score = 4;
        } else if (isTwoPairs(joker)) {
            score = 3;
        } else if (isOnePair(joker)) {
            score = 2;
        } else {
            score = 1;
        }

        return score;
    }

    private boolean isOnePair(boolean joker) {
        Map<String, Integer> cardCount = new HashMap<String, Integer>();
        for (String card : getCards(joker)) {
            if (cardCount.containsKey(card)) {
                cardCount.put(card, cardCount.get(card) + 1);
            } else {
                cardCount.put(card, 1);
            }
        }

        int pairs = 0;
        for (Integer count : cardCount.values()) {
            if (count == 2) {
                pairs++;
            }
        }

        return pairs == 1;
    }

    private boolean isTwoPairs(boolean joker) {
        Map<String, Integer> cardCount = new HashMap<String, Integer>();
        for (String card : getCards(joker)) {
            if (cardCount.containsKey(card)) {
                cardCount.put(card, cardCount.get(card) + 1);
            } else {
                cardCount.put(card, 1);
            }
        }

        int pairs = 0;
        for (Integer count : cardCount.values()) {
            if (count == 2) {
                pairs++;
            }
        }

        return pairs == 2;
    }

    private boolean isThreeOfAKind(boolean joker) {
        Map<String, Integer> cardCount = new HashMap<String, Integer>();
        for (String card : getCards(joker)) {
            if (cardCount.containsKey(card)) {
                cardCount.put(card, cardCount.get(card) + 1);
            } else {
                cardCount.put(card, 1);
            }
        }

        return cardCount.containsValue(3);
    }

    private boolean isFullHouse(boolean joker) {
        return isThreeOfAKind(joker) && isOnePair(joker);
    }

    private boolean isFourOfAKind(boolean joker) {
        Map<String, Integer> cardCount = new HashMap<String, Integer>();
        for (String card : getCards(joker)) {
            if (cardCount.containsKey(card)) {
                cardCount.put(card, cardCount.get(card) + 1);
            } else {
                cardCount.put(card, 1);
            }
        }

        return cardCount.containsValue(4);
    }

    private boolean isFiveOfAKind(boolean joker) {
        return new HashSet<String>(getCards(joker)).size() == 1;
    }

    @Override
    public int compareTo(Hand o) {
        if (this.score == o.score) {
            for (int i = 0; i < this.cards.size(); i++) {
                if (this.cards.get(i).getStrength() != o.cards.get(i).getStrength()) {
                    return this.cards.get(i).getStrength() - o.cards.get(i).getStrength();
                }
            }
        }

        return this.score - o.score;
    }
}
