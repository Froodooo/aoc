import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day06Test {
    @Test
    public void testA() {
        Day06 day06 = new Day06(Utils.readFile("aoc23\\input\\06_sample.txt"));
        assertEquals(288, day06.partA());
    }

    @Test
    public void testB() {
        Day06 day06 = new Day06(Utils.readFile("aoc23\\input\\06_sample.txt"));
        assertEquals(71503, day06.partB());
    }
}
