import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day18b.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day18/day18_ex.txt");
  assertEquals(solve(input), 3993);
});

Deno.test("Day 18", async () => {
  const input = await Deno.readTextFile("./day18/day18.txt");
  assertEquals(solve(input), 4784);
});
