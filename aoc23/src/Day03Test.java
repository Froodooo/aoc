import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day03Test {
    @Test
    public void testA() {
        Day03 day03 = new Day03(Utils.readFile("aoc23\\input\\03_sample.txt"));
        assertEquals(4361, day03.partA());
    }

    @Test
    public void testB() {
        Day03 day03 = new Day03(Utils.readFile("aoc23\\input\\03_sample.txt"));
        assertEquals(467835, day03.partB());
    }
}
