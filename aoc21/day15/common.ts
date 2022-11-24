import { BinaryHeap } from "https://deno.land/x/collections@v0.10.2/binary_heap.ts";

type queueElement = { risk: number; coordinate: Coordinate };

export class Coordinate {
  x: number;
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }

  isVisited(visited: Set<string>) {
    return visited.has(`${this.x},${this.y}`);
  }

  isInCave(cave: number[][]) {
    return this.x >= 0 && this.y >= 0 && this.x < cave[0].length &&
      this.y < cave.length;
  }

  isFinish(cave: number[][]): boolean {
    return this.x === cave[0].length - 1 && this.y === cave.length - 1;
  }
}

const directions = [
  new Coordinate(-1, 0),
  new Coordinate(0, -1),
  new Coordinate(1, 0),
  new Coordinate(0, 1),
];

function initVisited(start: Coordinate): Set<string> {
  const visited = new Set<string>();
  visited.add(`${start.x},${start.y}`);

  return visited;
}

function initQueue(start: Coordinate): BinaryHeap<queueElement> {
  const heapSortFn = (a: queueElement, b: queueElement) => a.risk - b.risk;
  const queue = new BinaryHeap<queueElement>(heapSortFn);
  queue.push({ risk: 0, coordinate: start });

  return queue;
}

export function findLowestRisk(
  start: Coordinate,
  cave: number[][],
): number {
  const visited = initVisited(start);
  const queue = initQueue(start);

  while (!queue.isEmpty()) {
    const { risk: risk, coordinate: coordinate } = queue.pop()!;

    if (coordinate.isFinish(cave)) {
      return risk;
    }

    for (const direction of directions) {
      const neighbourCoordinate = new Coordinate(
        coordinate.x + direction.x,
        coordinate.y + direction.y,
      );
      if (
        neighbourCoordinate.isInCave(cave) &&
        !neighbourCoordinate.isVisited(visited)
      ) {
        queue.push({
          risk: risk + cave[neighbourCoordinate.y][neighbourCoordinate.x],
          coordinate: neighbourCoordinate,
        });
        visited.add(`${neighbourCoordinate.x},${neighbourCoordinate.y}`);
      }
    }
  }

  throw new Error("No path found");
}

export function readCave(input: string): number[][] {
  return input.split("\n").map((line) =>
    line.split("").map((position) => +position)
  );
}
