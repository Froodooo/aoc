import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day10Test {
    @Test
    public void testA() {
        Day10 day10Sample1 = new Day10(Utils.readFile("aoc23\\input\\10_sample1.txt"));
        assertEquals(4, day10Sample1.partA());

        Day10 day10Sample2 = new Day10(Utils.readFile("aoc23\\input\\10_sample2.txt"));
        assertEquals(8, day10Sample2.partA());
    }

    @Test
    public void testB() {
        Day10 day10Sample3 = new Day10(Utils.readFile("aoc23\\input\\10_sample3.txt"));
        assertEquals(4, day10Sample3.partB());

        Day10 day10Sample4 = new Day10(Utils.readFile("aoc23\\input\\10_sample4.txt"));
        assertEquals(4, day10Sample4.partB());

        Day10 day10Sample5 = new Day10(Utils.readFile("aoc23\\input\\10_sample5.txt"));
        assertEquals(8, day10Sample5.partB());

        Day10 day10Sample6 = new Day10(Utils.readFile("aoc23\\input\\10_sample6.txt"));
        assertEquals(10, day10Sample6.partB());
    }
}
