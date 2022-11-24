import { Coordinate, findLowestRisk, readCave } from "./common.ts";

const input = await Deno.readTextFile("./day15/day15.txt");

export function solve(input: string): number {
  const cave = readCave(input);
  const start = new Coordinate(0, 0);
  const lowestRisk = findLowestRisk(start, cave);

  return lowestRisk;
}

console.log(solve(input));
