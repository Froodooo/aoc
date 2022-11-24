import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { solve } from "./day16a.ts";

Deno.test("Example 1", () => {
  const input = "8A004A801A8002F478";
  assertEquals(solve(input), 16);
});

Deno.test("Example 2", () => {
  const input = "620080001611562C8802118E34";
  assertEquals(solve(input), 12);
});

Deno.test("Example 3", () => {
  const input = "C0015000016115A2E0802F182340";
  assertEquals(solve(input), 23);
});

Deno.test("Example 4", () => {
  const input = "A0016C880162017C3686B18A3D4780";
  assertEquals(solve(input), 31);
});

Deno.test("Day 16", () => {
  const input = await Deno.readTextFile("./day16/day16.txt");
  assertEquals(solve(input), 895);
});
