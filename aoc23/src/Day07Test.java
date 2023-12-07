import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day07Test {
    @Test
    public void testA() {
        Day07 day07 = new Day07(Utils.readFile("aoc23\\input\\07_sample.txt"));
        assertEquals(6440, day07.partA());
    }

    @Test
    public void testB() {
        Day07 day07 = new Day07(Utils.readFile("aoc23\\input\\07_sample.txt"));
        assertEquals(5905, day07.partB());
    }
}
