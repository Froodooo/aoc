import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { visitPoints } from "./common.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day5/day5_ex.txt");
  const paths = input.split("\n");
  const visitedPoints = visitPoints(paths, { skipDiagonals: true });

  const multipleOverlaps =
    [...visitedPoints.values()].filter((point) => point > 1).length;
  assertEquals(multipleOverlaps, 5);
});

Deno.test("Day 5", async () => {
  const input = await Deno.readTextFile("./day5/day5.txt");
  const paths = input.split("\n");
  const visitedPoints = visitPoints(paths, { skipDiagonals: true });

  const multipleOverlaps =
    [...visitedPoints.values()].filter((point) => point > 1).length;
  assertEquals(multipleOverlaps, 4993);
});
