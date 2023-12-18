import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day18Test {
    @Test
    public void testA() {
        Day18 day18Sample = new Day18(Utils.readFile("aoc23\\input\\18_sample.txt"));
        assertEquals(62, day18Sample.partA());
    }

    @Test
    public void testB() {
        Day18 day18Sample = new Day18(Utils.readFile("aoc23\\input\\18_sample.txt"));
        assertEquals(952408144115L, day18Sample.partB());
    }
}
