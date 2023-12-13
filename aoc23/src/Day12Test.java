import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day12Test {
    @Test
    public void testA() {
        Day12 day12Sample = new Day12(Utils.readFile("aoc23\\input\\12_sample.txt"));
        assertEquals(21, day12Sample.partA());
    }
}
