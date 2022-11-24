import { Coordinate, findLowestRisk, readCave } from "./common.ts";

const input = await Deno.readTextFile("./day15/day15.txt");

function expandCave(cave: number[][], expansion: number): number[][] {
  const expandedCave = new Array(cave.length * expansion).fill(0).map(() =>
    new Array(cave[0].length * expansion).fill(0)
  );

  for (let y = 0; y < expandedCave.length; y++) {
    for (let x = 0; x < expandedCave[y].length; x++) {
      const modX = x % cave[0].length;
      const modY = y % cave.length;
      const dupX = Math.floor(x / cave[0].length);
      const dupY = Math.floor(y / cave.length);

      let newValue = cave[modY][modX] + (dupX + dupY);
      if (newValue > 9) {
        newValue = newValue % 10 + 1;
      }
      expandedCave[y][x] = newValue;
    }
  }

  return expandedCave;
}

export function solve(input: string): number {
  const cave = readCave(input);
  const expandedCave = expandCave(cave, 5);
  const start = new Coordinate(0, 0);
  const lowestRisk = findLowestRisk(start, expandedCave);

  return lowestRisk;
}

console.log(solve(input));
