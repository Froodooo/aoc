import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day11Test {
    @Test
    public void testA() {
        Day11 day11Sample1 = new Day11(Utils.readFile("aoc23\\input\\11_sample.txt"), 1);
        assertEquals(374, day11Sample1.partA());
    }

    @Test
    public void testB() {
        Day11 day11Sample1 = new Day11(Utils.readFile("aoc23\\input\\11_sample.txt"), 10);
        assertEquals(1030, day11Sample1.partB());

        Day11 day11Sample2 = new Day11(Utils.readFile("aoc23\\input\\11_sample.txt"), 100);
        assertEquals(8410, day11Sample2.partB());
    }
}
