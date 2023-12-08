import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day08 {
    private static String START_NODE = "AAA";
    private static String FINISH_NODE = "ZZZ";

    private String input;

    public Day08(String input) {
        this.input = input;
    }

    public int partA() {
        String[] instructions = getInstructions();
        Map<String, String[]> network = getNetwork();

        String currentNode = START_NODE;
        int hops = 0;
        while (!currentNode.equals(FINISH_NODE)) {
            String instruction = instructions[hops % instructions.length];
            String[] directions = network.get(currentNode);
            currentNode = instruction.equals("R") ? directions[1] : directions[0];
            hops++;
        }

        return hops;
    }

    public long partB() {
        String[] instructions = getInstructions();
        Map<String, String[]> network = getNetwork();

        List<String> currentNodes = network.keySet().stream().filter(node -> node.endsWith("A")).toList();

        List<Integer> allHops = new ArrayList<Integer>();
        for (String currentNode : currentNodes) {
            int hops = 0;
            while (!currentNode.endsWith("Z")) {
                String instruction = instructions[hops % instructions.length];
                String[] directions = network.get(currentNode);
                currentNode = instruction.equals("R") ? directions[1] : directions[0];
                hops++;
            }
            allHops.add(hops);
        }

        long lcm = allHops.get(0);
        for (int i = 1; i < allHops.size(); i++) {
            lcm = lcm(lcm, allHops.get(i));
        }

        return lcm;
    }

    private long lcm(long a, long b) {
        return a * (b / gcd(a, b));
    }

    private long gcd(long a, long b) {
        while (b > 0) {
            long temp = b;
            b = a % b; // % is remainder
            a = temp;
        }

        return a;
    }

    private String[] getInstructions() {
        return input.split("\n\n")[0].split("");
    }

    private Map<String, String[]> getNetwork() {
        Map<String, String[]> network = new HashMap<String, String[]>();
        String[] nodes = input.split("\n\n")[1].split("\n");
        for (String node : nodes) {
            String lhs = node.split("=")[0].trim();
            String[] rhs = node.split("=")[1].replace("(", "").replace(")", "").replace(",", "").trim().split(" ");
            network.put(lhs, rhs);
        }

        return network;
    }
}
