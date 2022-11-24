import * as common from "./common.ts";

const input = await Deno.readTextFile("./day11/day11.txt");

export function solve(input: string): number {
  const octopuses = common.readOctopuses(input);

  let flashes = 0;
  for (let i = 0; i < 100; i++) {
    flashes += common.step(octopuses);
  }

  return flashes;
}

console.log(solve(input));
