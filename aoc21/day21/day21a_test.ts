import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day21a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day21/day21_ex.txt");
  assertEquals(solve(input), 739785);
});

Deno.test("Day 21", async () => {
  const input = await Deno.readTextFile("./day21/day21.txt");
  assertEquals(solve(input), 432450);
});
