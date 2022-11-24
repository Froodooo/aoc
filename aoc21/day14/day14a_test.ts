import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day14a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day14/day14_ex.txt");
  assertEquals(solve(input), 1588);
});

Deno.test("Day 14", async () => {
  const input = await Deno.readTextFile("./day14/day14.txt");
  assertEquals(solve(input), 3259);
});
