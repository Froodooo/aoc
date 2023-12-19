import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day19Test {
    @Test
    public void testA() {
        Day19 day19Sample = new Day19(Utils.readFile("aoc23\\input\\19_sample.txt"));
        assertEquals(19114, day19Sample.partA());
    }

    @Test
    public void testB() {
        Day19 day19Sample = new Day19(Utils.readFile("aoc23\\input\\19_sample.txt"));
        assertEquals(-1, day19Sample.partB());
    }
}
