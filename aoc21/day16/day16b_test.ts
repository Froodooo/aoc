import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day16b.ts";

Deno.test("Example 1", () => {
  const input = "C200B40A82";
  assertEquals(solve(input), 3);
});

Deno.test("Example 2", () => {
  const input = "04005AC33890";
  assertEquals(solve(input), 54);
});

Deno.test("Example 3", () => {
  const input = "880086C3E88112";
  assertEquals(solve(input), 7);
});

Deno.test("Example 4", () => {
  const input = "CE00C43D881120";
  assertEquals(solve(input), 9);
});

Deno.test("Example 5", () => {
  const input = "D8005AC2A8F0";
  assertEquals(solve(input), 1);
});

Deno.test("Example 6", () => {
  const input = "F600BC2D8F";
  assertEquals(solve(input), 0);
});

Deno.test("Example 7", () => {
  const input = "9C005AC2F8F0";
  assertEquals(solve(input), 0);
});

Deno.test("Example 8", () => {
  const input = "9C0141080250320F1802104A08";
  assertEquals(solve(input), 1);
});

Deno.test("Day 16", async () => {
  const input = await Deno.readTextFile("./day16/day16.txt");
  assertEquals(solve(input), 1148595959144);
});
