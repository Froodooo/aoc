import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day13Test {
    @Test
    public void testA() {
        Day13 day13Sample = new Day13(Utils.readFile("aoc23\\input\\13_sample.txt"));
        assertEquals(405, day13Sample.partA());
    }

    @Test
    public void testB() {
        Day13 day13Sample = new Day13(Utils.readFile("aoc23\\input\\13_sample.txt"));
        assertEquals(400, day13Sample.partB());
    }
}
