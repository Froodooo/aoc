import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day15Test {
    @Test
    public void testA() {
        Day15 day15Sample = new Day15(Utils.readFile("aoc23\\input\\15_sample.txt"));
        assertEquals(1320, day15Sample.partA());
    }

    @Test
    public void testB() {
        Day15 day15Sample = new Day15(Utils.readFile("aoc23\\input\\15_sample.txt"));
        assertEquals(145, day15Sample.partB());
    }
}
