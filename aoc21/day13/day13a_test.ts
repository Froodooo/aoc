import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day13a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day13/day13_ex.txt");
  assertEquals(solve(input), 17);
});

Deno.test("Day 13", async () => {
  const input = await Deno.readTextFile("./day13/day13.txt");
  assertEquals(solve(input), 675);
});
