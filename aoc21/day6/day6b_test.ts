import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./common.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day6/day6_ex.txt");
  assertEquals(solve(input, 256), 26984457539);
});

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day6/day6.txt");
  assertEquals(solve(input, 256), 1705008653296);
});
