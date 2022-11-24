import { neighbours } from "./constants.ts";

const input = await Deno.readTextFile("./day9/day9.txt");

function readMap(input: string): number[][] {
  return input.split("\n").map((row) =>
    row.split("").map((point) => parseInt(point))
  );
}

function getLowPoints(map: number[][]): number[] {
  const lowPoints = [];

  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
      const neighbourPoints: number[] = [];
      neighbours.forEach((neighbour) => {
        const neighbourPoint = { x: x + neighbour.x, y: y + neighbour.y };
        if (
          neighbourPoint.x >= 0 && neighbourPoint.y >= 0 &&
          neighbourPoint.x < map[y].length && neighbourPoint.y < map.length
        ) {
          neighbourPoints.push(map[neighbourPoint.y][neighbourPoint.x]);
        }
      });

      const currentPoint = map[y][x];
      if (neighbourPoints.every((point) => point > currentPoint)) {
        lowPoints.push(currentPoint);
      }
    }
  }
  return lowPoints;
}

export function solve(input: string): number {
  const map = readMap(input);
  const lowPoints = getLowPoints(map);
  const riskLevel = lowPoints.reduce((sum, point) => sum + point + 1, 0);
  return riskLevel;
}

console.log(solve(input));
