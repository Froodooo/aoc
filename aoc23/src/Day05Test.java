import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day05Test {
    @Test
    public void testA() {
        Day05 day05 = new Day05(Utils.readFile("aoc23\\input\\05_sample.txt"));
        assertEquals(35, day05.partA());
    }

    @Test
    public void testB() {
        Day05 day05 = new Day05(Utils.readFile("aoc23\\input\\05_sample.txt"));
        assertEquals(46, day05.partB());
    }
}
