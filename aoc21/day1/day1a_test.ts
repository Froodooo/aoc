import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { countIncreases } from "./day1a.ts";

Deno.test("Example 1", async () => {
  const testInput = await Deno.readTextFile("./day1/day1_ex.txt");
  assertEquals(
    countIncreases(
      testInput.split("\n").map((measurement) => parseInt(measurement)),
    ),
    7,
  );
});

Deno.test("Day 1a", async () => {
  const testInput = await Deno.readTextFile("./day1/day1.txt");
  assertEquals(
    countIncreases(
      testInput.split("\n").map((measurement) => parseInt(measurement)),
    ),
    1482,
  );
});
