const input = await Deno.readTextFile("./day17/day17.txt");

function getTriangleNumber(n: number): number {
  return (n * (n + 1)) / 2;
}

function findHighY(yMax: number): number {
  return getTriangleNumber(Math.abs(yMax) - 1);
}

function readRanges(input: string): number[][] {
  return input.replace("target area: ", "").split(", ").map((range) =>
    range.substring(2)
  ).map((range) => range.split("..").map((point) => +point));
}

export function solve(input: string): number {
  const [[_xMin, _xMax], [yMax, _yMin]] = readRanges(input);
  return findHighY(yMax);
}

console.log(solve(input));
