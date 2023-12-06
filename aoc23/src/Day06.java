import java.util.Arrays;

public class Day06 {
    private String input;

    public Day06(String input) {
        this.input = input;
    }

    public int partA() {
        String[] document = input.split("\n");
        int[] times = Arrays.stream(document[0].replace("Time:", "").trim().split("\\s+")).mapToInt(Integer::parseInt)
                .toArray();
        int[] winningDistances = Arrays.stream(document[1].replace("Distance:", "").trim().split("\\s+"))
                .mapToInt(Integer::parseInt)
                .toArray();

        int winSum = 1;
        for (int i = 0; i < times.length; i++) {
            int time = times[i];
            int winningDistance = winningDistances[i];
            winSum *= calculateWins(time, winningDistance);
        }

        return winSum;
    }

    public long partB() {
        String[] document = input.split("\n");
        Long time = Long.parseLong(document[0].replace("Time:", "").trim().replaceAll("\\s+", ""));
        Long distance = Long.parseLong(document[1].replace("Distance:", "").trim().replaceAll("\\s+", ""));

        long wins = calculateWins(time, distance);

        return wins;
    }

    private long calculateWins(long time, long winningDistance) {
        long wins = 0;
        for (int i = 0; i < time; i++) {
            long distance = calculateDistance(time, i);
            if (distance > winningDistance) {
                wins++;
            }
        }

        return wins;
    }

    private long calculateDistance(long time, long holdButtonTime) {
        return (time - holdButtonTime) * holdButtonTime;
    }
}
