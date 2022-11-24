import { fold, readDots, readInstructions } from "./common.ts";

const input = await Deno.readTextFile("./day13/day13.txt");

export function solve(input: string): number {
  const [rawDots, rawInstructions] = input.split("\n\n");
  const dots = readDots(rawDots);
  const instructions = readInstructions(rawInstructions);

  const foldedCoordinates = fold(dots, instructions[0]);

  return foldedCoordinates.length;
}

console.log(solve(input));
