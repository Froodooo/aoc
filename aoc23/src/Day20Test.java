import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day20Test {
    @Test
    public void testA() {
        Day20 day20Sample1 = new Day20(Utils.readFile("aoc23\\input\\20_sample1.txt"));
        assertEquals(32000000, day20Sample1.partA());

        Day20 day20Sample2 = new Day20(Utils.readFile("aoc23\\input\\20_sample2.txt"));
        assertEquals(11687500, day20Sample2.partA());
    }

    @Test
    public void testB() {
        Day20 day20Sample = new Day20(Utils.readFile("aoc23\\input\\20_sample.txt"));
        assertEquals(-1, day20Sample.partB());
    }
}
