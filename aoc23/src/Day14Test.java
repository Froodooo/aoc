import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day14Test {
    @Test
    public void testA() {
        Day14 day14Sample = new Day14(Utils.readFile("aoc23\\input\\14_sample.txt"));
        assertEquals(136, day14Sample.partA());
    }

    @Test
    public void testB() {
        Day14 day14Sample = new Day14(Utils.readFile("aoc23\\input\\14_sample.txt"));
        assertEquals(-1, day14Sample.partB());
    }
}
