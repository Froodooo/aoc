import day22.Snapshot;

public class Day22 {
    private String input;

    public Day22(String input) {
        this.input = input;
    }

    public int partA() {
        Snapshot snapshot = new Snapshot(input);
        System.out.println(snapshot.toString());
        return -1;
    }

    public long partB() {
        return -1;
    }
}