import { readChunk } from "./common.ts";

const input = await Deno.readTextFile("./day10/day10.txt");

function calculatePoints(character: string): number {
  switch (character) {
    case ")":
      return 1;
    case "]":
      return 2;
    case "}":
      return 3;
    case ">":
      return 4;
    default:
      return 0;
  }
}

export function solve(input: string): number {
  const lines = input.split("\n").map((line) => line.split(""));

  const incompleteLines = lines.filter((line) =>
    readChunk([...line], [])[0] === undefined
  );
  const closeCharacterLines = incompleteLines.map((line) =>
    readChunk(line, [], false)
  );
  const points = closeCharacterLines.map(
    (closeCharacters) =>
      closeCharacters.reduce(
        (total, character) => total * 5 + calculatePoints(character),
        0,
      ),
  ).sort((a, b) => a - b);
  const middleScore = points[Math.floor(points.length / 2)];

  return middleScore;
}

console.log(solve(input));
