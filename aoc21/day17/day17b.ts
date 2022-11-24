const input = await Deno.readTextFile("./day17/day17_ex.txt");

function range(point1: number, point2: number): number[] {
  const result = [];
  if (point1 > point2) {
    for (let i = point1; i >= point2; i--) {
      result.push(i);
    }
  } else {
    for (let i = point1; i <= point2; i++) {
      result.push(i);
    }
  }

  return result;
}

function getTriangleNumber(n: number): number {
  return (n * (n + 1)) / 2;
}

function isInTarget(
  x: number,
  y: number,
  xRange: number[],
  yRange: number[],
) {
  let xPos = 0;
  let yPos = 0;
  let xVel = x;
  let yVel = y;

  while (
    xPos <= xRange[xRange.length - 1] && yPos >= yRange[yRange.length - 1]
  ) {
    xPos += xVel;
    yPos += yVel;

    if (xRange.includes(xPos) && yRange.includes(yPos)) {
      return true;
    }

    xVel = xVel > 0 ? xVel - 1 : xVel;
    yVel -= 1;
  }

  return false;
}

function directHits(
  xRange: number[],
  yRange: number[],
): number {
  return xRange.length * yRange.length;
}

function indirectHits(
  xRangeProbe: number[],
  yRangeProbe: number[],
  xRangeTarget: number[],
  yRangeTarget: number[],
) {
  let counter = 0;

  for (const x of xRangeProbe) {
    for (const y of yRangeProbe) {
      if (isInTarget(x, y, xRangeTarget, yRangeTarget)) {
        counter += 1;
      }
    }
  }

  return counter;
}

function findLowX(xMin: number, xMax: number): number {
  let x = 1;

  while (x <= xMax) {
    const triangleNumber = getTriangleNumber(x);
    if (triangleNumber >= xMin && triangleNumber <= xMax) {
      return x;
    }

    x += 1;
  }

  return x;
}

function readRanges(input: string): number[][] {
  return input.replace("target area: ", "").split(", ").map((range) =>
    range.substring(2)
  ).map((range) => range.split("..").map((point) => +point));
}

export function solve(input: string): number {
  const [[xMin, xMax], [yMax, yMin]] = readRanges(input);

  const lowX = findLowX(xMin, xMax);
  const highX = xMax / 2;
  const lowY = yMax;
  const highY = Math.abs(yMax) - 1;

  const xRangeTarget = range(xMin, xMax);
  const yRangeTarget = range(yMin, yMax);
  const xRangeProbe = range(lowX, highX);
  const yRangeProbe = range(lowY, highY);

  let counter = 0;

  counter += directHits(xRangeTarget, yRangeTarget);
  counter += indirectHits(xRangeProbe, yRangeProbe, xRangeTarget, yRangeTarget);

  return counter;
}

console.log(solve(input));
