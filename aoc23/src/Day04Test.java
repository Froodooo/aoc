import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day04Test {
    @Test
    public void testA() {
        Day04 day04 = new Day04(Utils.readFile("aoc23\\input\\04_sample.txt"));
        assertEquals(13, day04.partA());
    }

    @Test
    public void testB() {
        Day04 day04 = new Day04(Utils.readFile("aoc23\\input\\04_sample.txt"));
        assertEquals(30, day04.partB());
    }
}
