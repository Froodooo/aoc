import * as common from "./common.ts";

const input = await Deno.readTextFile("./day11/day11.txt");

function isSimultaneousFlash(octopuses: number[][]): boolean {
  return octopuses.every((line) => line.every((octopus) => octopus === 0));
}

export function solve(input: string): number {
  const octopuses = common.readOctopuses(input);

  let rounds = 0;
  while (!isSimultaneousFlash(octopuses)) {
    common.step(octopuses);
    rounds += 1;
  }

  return rounds;
}

console.log(solve(input));
