import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import day07.Hand;

public class Day07 {
    private String input;

    public Day07(String input) {
        this.input = input;
    }

    public int partA() {
        String[] lines = input.split("\n");
        List<Hand> hands = new ArrayList<Hand>();
        for(String line : lines) {
            String[] parts = line.split(" ");
            hands.add(new Hand(parts[0], Integer.parseInt(parts[1]), false));
        }

        Collections.sort(hands);

        int totalWinnings = 0;
        for (int i = 0; i < hands.size(); i++) {
            totalWinnings += hands.get(i).getBid() * (i + 1);
        }

        return totalWinnings;
    }

    public long partB() {
        String[] lines = input.split("\n");
        List<Hand> hands = new ArrayList<Hand>();
        for(String line : lines) {
            String[] parts = line.split(" ");
            hands.add(new Hand(parts[0], Integer.parseInt(parts[1]), true));
        }

        
        int counter = 1;
        for (Hand hand : hands) {
            System.out.println(counter + ": " + hand.toString());
            counter++;
        }
        
        Collections.sort(hands);

        long totalWinnings = 0;
        for (int i = 0; i < hands.size(); i++) {
            totalWinnings += hands.get(i).getBid() * (i + 1);
        }

        return totalWinnings;
    }
}
