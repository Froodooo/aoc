import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day22a.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day22/day22_ex1.txt");
  assertEquals(solve(input), 39);
});

Deno.test("Example 2", async () => {
  const input = await Deno.readTextFile("./day22/day22_ex2.txt");
  assertEquals(solve(input), 590784);
});

Deno.test("Day 22", async () => {
  const input = await Deno.readTextFile("./day22/day22.txt");
  assertEquals(solve(input), 623748);
});
