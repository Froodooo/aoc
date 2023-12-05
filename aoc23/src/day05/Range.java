package day05;

public class Range {
    long sourceStart;
    long destionationStart;
    long range;
    
    public Range(long sourceStart, long destionationStart, long range) {
        this.sourceStart = sourceStart;
        this.destionationStart = destionationStart;
        this.range = range;
    }

    public boolean isInRange(long value) {
        return value >= sourceStart && value < sourceStart + range;
    }

    public long getDestination(long value) {
        return destionationStart + (value - sourceStart);
    }

    public String toString() {
        return sourceStart + " " + destionationStart + " " + range;
    }
}
