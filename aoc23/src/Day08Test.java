import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day08Test {
    @Test
    public void testA() {
        Day08 day08Sample1 = new Day08(Utils.readFile("aoc23\\input\\08_sample1.txt"));
        assertEquals(2, day08Sample1.partA());

        Day08 day08Sample2 = new Day08(Utils.readFile("aoc23\\input\\08_sample2.txt"));
        assertEquals(6, day08Sample2.partA());
    }

    @Test
    public void testB() {
        Day08 day08 = new Day08(Utils.readFile("aoc23\\input\\08_sample3.txt"));
        assertEquals(6, day08.partB());
    }
}
