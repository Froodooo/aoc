import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./common.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day7/day7_ex.txt");
  assertEquals(solve(input, { isSummed: false }), 37);
});

Deno.test("Day 7", async () => {
  const input = await Deno.readTextFile("./day7/day7.txt");
  assertEquals(solve(input, { isSummed: false }), 340056);
});
