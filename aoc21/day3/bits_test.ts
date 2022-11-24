import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { countBits } from "./bits.ts";

Deno.test("countBits", () => {
  assertEquals(countBits(["101", "011"]), [1, 1, 2]);
  assertEquals(countBits(["1101", "0011"]), [1, 1, 1, 2]);
  assertEquals(countBits(["0000", "1111"]), [1, 1, 1, 1]);
  assertEquals(countBits(["0000", "0000"]), [0, 0, 0, 0]);
});
