import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { co2Scrubber, oxygen } from "./day3b.ts";

Deno.test("oxygen", () => {
  assertEquals(oxygen(["111", "100", "011"]), 7);
});

Deno.test("co2_scrubber", () => {
  assertEquals(co2Scrubber(["111", "100", "011"]), 3);
});

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day3/day3_ex.txt");
  const binaries = input.split("\n");
  const oxygenNumber = oxygen(binaries);
  assertEquals(oxygenNumber, 23);

  const co2ScrubberNumber = co2Scrubber(binaries);
  assertEquals(co2ScrubberNumber, 10);
});

Deno.test("Day 3", async () => {
  const input = await Deno.readTextFile("./day3/day3.txt");
  const binaries = input.split("\n");
  const oxygenNumber = oxygen(binaries);
  const co2ScrubberNumber = co2Scrubber(binaries);

  assertEquals(oxygenNumber * co2ScrubberNumber, 6940518);
});
