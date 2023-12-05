package day05;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class Category {
    private String source;
    private String destination;
    private List<Range> ranges;

    public Category(String source, String destination) {
        this.source = source;
        this.destination = destination;
        this.ranges = new ArrayList<Range>();
    }

    public Category(String map) {
        this.ranges = new ArrayList<Range>();

        String[] lines = map.split("\n");
        String[] header = lines[0].replace(":", "").split("-");

        this.source = header[0];
        this.destination = header[2].split(" ")[0];

        for (int j = 1; j < lines.length; j++) {
            long[] line = Stream.of(lines[j].split(" ")).mapToLong(Long::parseLong).toArray();
            addRange(line[1], line[0], line[2]);
        }
    }

    public String getSource() {
        return source;
    }

    public String getDestination() {
        return destination;
    }

    public long getDestination(long value) {
        for (Range range : ranges) {
            if (range.isInRange(value)) {
                return range.getDestination(value);
            }
        }

        return value;
    }

    public void addRange(long sourceStart, long destionationStart, long range) {
        ranges.add(new Range(sourceStart, destionationStart, range));
    }

    public String toString() {
        return "Source: " + source + ", Destination: " + destination + "\nRanges: " + ranges.toString() + "\n";
    }
}
