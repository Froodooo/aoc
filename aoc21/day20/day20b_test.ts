import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day20b.ts";

// Deno.test("Example 1", async () => {
//   const input = await Deno.readTextFile("./day20/day20_ex.txt");
//   assertEquals(solve(input, 50), 3351);
// });

Deno.test("Day 20", async () => {
  const input = await Deno.readTextFile("./day20/day20.txt");
  assertEquals(solve(input, 50), 16112);
});
