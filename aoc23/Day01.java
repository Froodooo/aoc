package aoc23;

import java.util.Arrays;

public class Day01 {
    public static void main(String[] args) {
        String content = Utils.readFile("01.txt");
        String[] separatedContent = Utils.separateValues(content, "\n");
        System.out.println(Arrays.toString(separatedContent));
    }
}