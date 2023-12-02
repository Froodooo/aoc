import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day01Test {
    @Test
    public void testA() {
        Day01 day01 = new Day01(Utils.readFile("aoc23\\input\\01_sample.txt"));
        assertEquals(142, day01.partA());
    }

    @Test
    public void testB() {
        Day01 day01 = new Day01(Utils.readFile("aoc23\\input\\01_sample2.txt"));
        assertEquals(281, day01.partB());
    }
}
