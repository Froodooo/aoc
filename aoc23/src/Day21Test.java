import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day21Test {
    @Test
    public void testA() {
        Day21 day21Sample1 = new Day21(Utils.readFile("aoc23\\input\\21_sample.txt"));
        assertEquals(16, day21Sample1.partA());
    }

    @Test
    public void testB() {
        Day21 day21Sample = new Day21(Utils.readFile("aoc23\\input\\21_sample.txt"));
        assertEquals(-1, day21Sample.partB());
    }
}
