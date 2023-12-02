import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day02Test {
    @Test
    public void testA() {
        Day02 day02 = new Day02(Utils.readFile("aoc23\\input\\02_sample.txt"));
        assertEquals(8, day02.partA());
    }

    @Test
    public void testB() {
        Day02 day02 = new Day02(Utils.readFile("aoc23\\input\\02_sample.txt"));
        assertEquals(2286, day02.partB());
    }
}
