import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day17Test {
    @Test
    public void testA() {
        Day17 day17Sample = new Day17(Utils.readFile("aoc23\\input\\17_sample.txt"));
        assertEquals(102, day17Sample.partA());
    }

    // @Test
    // public void testB() {
    //     Day17 day17Sample = new Day17(Utils.readFile("aoc23\\input\\17_sample.txt"));
    //     assertEquals(51, day17Sample.partB());
    // }
}
