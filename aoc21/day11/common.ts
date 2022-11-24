function stepNeighbour(
  x: number,
  y: number,
  octopuses: number[][],
  flashed: number[][],
): void {
  flashed[y][x] = 1;

  for (let dy = -1; dy <= 1; dy++) {
    for (let dx = -1; dx <= 1; dx++) {
      const xx = x + dx;
      const yy = y + dy;
      if (
        xx >= 0 && yy >= 0 && xx < octopuses[0].length &&
        yy < octopuses.length
      ) {
        octopuses[yy][xx] += 1;
        if (octopuses[yy][xx] >= 10 && flashed[yy][xx] === 0) {
          stepNeighbour(xx, yy, octopuses, flashed);
        }
      }
    }
  }
}

export function step(octopuses: number[][]): number {
  for (let y = 0; y < octopuses.length; y++) {
    for (let x = 0; x < octopuses[y].length; x++) {
      octopuses[y][x] += 1;
    }
  }

  const flashed = Array(octopuses.length).fill(0).map(() =>
    Array(octopuses[0].length).fill(0)
  );
  for (let y = 0; y < octopuses.length; y++) {
    for (let x = 0; x < octopuses[y].length; x++) {
      if (octopuses[y][x] === 10) {
        stepNeighbour(x, y, octopuses, flashed);
      }
    }
  }

  for (let y = 0; y < octopuses.length; y++) {
    for (let x = 0; x < octopuses[y].length; x++) {
      if (flashed[y][x] === 1) {
        octopuses[y][x] = 0;
      }
    }
  }

  return flashed.reduce(
    (total, line) =>
      total + line.reduce((lineTotal, value) => lineTotal + value, 0),
    0,
  );
}

export function readOctopuses(input: string): number[][] {
  return input.split("\n").map((line) =>
    line.split("").map((octopus) => parseInt(octopus))
  );
}
