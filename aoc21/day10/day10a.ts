import { readChunk } from "./common.ts";

const input = await Deno.readTextFile("./day10/day10.txt");

function calculatePoints(character: string): number {
  switch (character) {
    case ")":
      return 3;
    case "]":
      return 57;
    case "}":
      return 1197;
    case ">":
      return 25137;
    default:
      return 0;
  }
}

export function solve(input: string): number {
  const lines = input.split("\n").map((line) => line.split(""));

  const invalidCharacters = lines.map((line) => readChunk(line, [])[0]);
  const points = invalidCharacters.reduce(
    (total, character) => total + calculatePoints(character),
    0,
  );

  return points;
}

console.log(solve(input));
