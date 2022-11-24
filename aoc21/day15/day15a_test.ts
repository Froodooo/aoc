import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day15a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day15/day15_ex.txt");
  assertEquals(solve(input), 40);
});

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day15/day15.txt");
  assertEquals(solve(input), 472);
});
