import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day11a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day11/day11_ex.txt");
  assertEquals(solve(input), 1656);
});

Deno.test("Day 11", async () => {
  const input = await Deno.readTextFile("./day11/day11.txt");
  assertEquals(solve(input), 1755);
});
