import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day8b.ts";

Deno.test("Example 2", async () => {
  const input = await Deno.readTextFile("./day8/day8_ex2.txt");
  assertEquals(solve(input), 61229);
});

Deno.test("Day 8", async () => {
  const input = await Deno.readTextFile("./day8/day8.txt");
  assertEquals(solve(input), 1011823);
});
