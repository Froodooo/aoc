import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day09Test {
    @Test
    public void testA() {
        Day09 day09Sample1 = new Day09(Utils.readFile("aoc23\\input\\09_sample.txt"));
        assertEquals(114, day09Sample1.partA());
    }

    @Test
    public void testB() {
        Day09 day09 = new Day09(Utils.readFile("aoc23\\input\\09_sample.txt"));
        assertEquals(2, day09.partB());
    }
}
