import { visitPoints } from "./common.ts";

const input = await Deno.readTextFile("./day5/day5.txt");

const paths = input.split("\n");
const visitedPoints = visitPoints(paths, { skipDiagonals: false });

const multipleOverlaps =
  [...visitedPoints.values()].filter((point) => point > 1).length;

console.log(multipleOverlaps);
