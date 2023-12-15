import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

public class Day15 {
    private String input;

    public Day15(String input) {
        this.input = input;
    }

    public int partA() {
        int sum = 0;
        for (String step : input.trim().split(",")) {
            sum += getValue(step);
        }
        return sum;
    }

    public int partB() {
        HashMap<Integer, List<String>> boxes = initBoxes();
        for (String step : input.trim().split(",")) {
            String[] parts = step.split("(-|=)");
            int box = getValue(parts[0]);
            if (step.contains("=")) {
                String lens = String.format("%s %d", parts[0], Integer.parseInt(parts[1]));
                int contains = contains(boxes.get(box), parts[0]);
                if (contains > -1) {
                    boxes.get(box).set(contains, lens);
                } else {
                    boxes.get(box).add(lens);
                }
            } else {
                boxes.get(box).removeIf(lbl -> lbl.startsWith(parts[0]));
            }
        }

        int power = focusingPower(boxes);

        return power;
    }

    private int focusingPower(HashMap<Integer, List<String>> boxes) {
        int power = 0;
        for (int i = 0; i < 256; i++) {
            List<String> box = boxes.get(i);
            for (int j = 0; j < box.size(); j++) {
                String[] parts = box.get(j).split(" ");
                int focalLength = Integer.parseInt(parts[1]);
                power += ((i + 1) * (j + 1) * focalLength);
            }
        }
        return power;
    }

    private int contains(List<String> box, String step) {
        for (int i = 0; i < box.size(); i++) {
            if (box.get(i).startsWith(step)) {
                return i;
            }
        }
        return -1;
    }

    private int getValue(String step) {
        int value = 0;
        for (String c : step.split("")) {
            value += (int) c.charAt(0);
            value *= 17;
            value %= 256;
        }
        return value;
    }

    private HashMap<Integer, List<String>> initBoxes() {
        HashMap<Integer, List<String>> boxes = new HashMap<>();
        for (int i = 0; i < 256; i++) {
            boxes.put(i, new LinkedList<String>());
        }
        return boxes;
    }
}
