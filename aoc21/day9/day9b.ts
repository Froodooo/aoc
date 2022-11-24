import { Point } from "./point.ts";
import { neighbours } from "./constants.ts";

const input = await Deno.readTextFile("./day9/day9.txt");

function readMap(input: string): number[][] {
  return input.split("\n").map((row) =>
    row.split("").map((point) => parseInt(point))
  );
}

function inBasin(basin: Point[], point: Point) {
  return basin.some((basinPoint) => basinPoint.isSame(point));
}

function getBasin(
  basin: Point[],
  map: number[][],
  point: Point,
): Point[] {
  basin.push(point);

  for (let i = 0; i < neighbours.length; i++) {
    const neighbour = neighbours[i];

    const neighbourPoint = new Point(
      point.x + neighbour.x,
      point.y + neighbour.y,
      0,
    );

    if (neighbourPoint.withinMap(map)) {
      neighbourPoint.setValue(map);
    } else {
      continue;
    }

    if (map[neighbourPoint.y][neighbourPoint.x] === 9) {
      continue;
    }

    if (neighbourPoint.isOption(point) && !inBasin(basin, neighbourPoint)) {
      basin = getBasin(basin, map, neighbourPoint);
    }
  }

  return basin;
}

function getBasins(map: number[][]): Point[][] {
  const basins = [];

  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
      const point = new Point(x, y, map[y][x]);

      if (point.value === 9 || point.inBasin(basins)) {
        continue;
      }

      basins.push(getBasin([], map, point));
    }
  }

  return basins;
}

export function solve(input: string): number {
  const map = readMap(input);
  const basins = getBasins(map);
  const sortedBasins = basins.sort((basin1, basin2) => {
    return basin2.length - basin1.length;
  });

  sortedBasins.splice(3);
  const multiple = sortedBasins.reduce(
    (total, basin) => total * basin.length,
    1,
  );

  return multiple;
}

console.log(solve(input));
