import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day9a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day9/day9_ex.txt");
  assertEquals(solve(input), 15);
});

Deno.test("Day 9", async () => {
  const input = await Deno.readTextFile("./day9/day9.txt");
  assertEquals(solve(input), 512);
});
