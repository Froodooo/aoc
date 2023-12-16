import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day16Test {
    @Test
    public void testA() {
        Day16 day16Sample = new Day16(Utils.readFile("aoc23\\input\\16_sample.txt"));
        assertEquals(46, day16Sample.partA());
    }

    @Test
    public void testB() {
        Day16 day16Sample = new Day16(Utils.readFile("aoc23\\input\\16_sample.txt"));
        assertEquals(51, day16Sample.partB());
    }
}
