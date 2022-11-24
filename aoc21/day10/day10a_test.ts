import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day10a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day10/day10_ex.txt");
  assertEquals(solve(input), 26397);
});

Deno.test("Day 10", async () => {
  const input = await Deno.readTextFile("./day10/day10.txt");
  assertEquals(solve(input), 358737);
});
