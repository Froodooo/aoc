import day17.Map;

public class Day17 {
    private String input;

    public Day17(String input) {
        this.input = input;

    }

    public int partA() {
        Map map = new Map(input);
        System.out.println(map.toString());
        return map.dijkstra();
    }

    public int partB() {
        return -1;
    }
}
