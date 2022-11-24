import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day18a.ts";

Deno.test("Examples", () => {
  const input1 = "[[1,2],[[3,4],5]]";
  assertEquals(solve(input1), 143);

  const input2 = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]";
  assertEquals(solve(input2), 1384);
});

Deno.test("Example data", async () => {
  const input = await Deno.readTextFile("./day18/day18_ex.txt");
  assertEquals(solve(input), 4140);
});

Deno.test("Day 18", async () => {
  const input = await Deno.readTextFile("./day18/day18.txt");
  assertEquals(solve(input), 4457);
});
