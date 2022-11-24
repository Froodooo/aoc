import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { epsilon, gamma } from "./day3a.ts";
import { countBits } from "./bits.ts";

Deno.test("gamma", () => {
  assertEquals(gamma([3, 3], 4), 3);
  assertEquals(gamma([1, 1], 4), 0);
});

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day3/day3_ex.txt");
  const binaries = input.split("\n");
  const positions = countBits(binaries);
  const gammaNumber = gamma(positions, binaries.length);
  assertEquals(gammaNumber, 22);

  const epsilonNumber = epsilon(positions, binaries.length);
  assertEquals(epsilonNumber, 9);
});

Deno.test("Day 3", async () => {
  const input = await Deno.readTextFile("./day3/day3.txt");
  const binaries = input.split("\n");
  const positions = countBits(binaries);
  const gammaNumber = gamma(positions, binaries.length);
  const epsilonNumber = epsilon(positions, binaries.length);

  assertEquals(gammaNumber * epsilonNumber, 3009600);
});
