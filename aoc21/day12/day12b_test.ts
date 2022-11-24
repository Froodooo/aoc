import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day12b.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day12/day12_ex1.txt");
  assertEquals(solve(input), 36);
});

Deno.test("Example 2", async () => {
  const input = await Deno.readTextFile("./day12/day12_ex2.txt");
  assertEquals(solve(input), 103);
});

Deno.test("Example 3", async () => {
  const input = await Deno.readTextFile("./day12/day12_ex3.txt");
  assertEquals(solve(input), 3509);
});

Deno.test("Day 12", async () => {
  const input = await Deno.readTextFile("./day12/day12.txt");
  assertEquals(solve(input), 99448);
});
