type visitPointOptions = { skipDiagonals: boolean };

export function visitPoints(
  paths: string[],
  options: visitPointOptions,
): Map<string, number> {
  return paths.reduce((visitedPoints, path: string) => {
    const [[x1, y1], [x2, y2]] = path.split(" -> ").map((point) =>
      point.split(",").map((part) => parseInt(part))
    );
    if (options.skipDiagonals && x1 != x2 && y1 != y2) return visitedPoints;

    const difference = Math.abs(x1 - x2) > 0
      ? Math.abs(x1 - x2) + 1
      : Math.abs(y1 - y2) + 1;

    const xPoints = generatePoints(x1, x2, difference);
    const yPoints = generatePoints(y1, y2, difference);

    for (let i = 0; i < difference; i++) {
      const overlaps = visitedPoints.get(`${xPoints[i]},${yPoints[i]}`) ?? 0;
      visitedPoints.set(`${xPoints[i]},${yPoints[i]}`, overlaps + 1);
    }

    return visitedPoints;
  }, new Map<string, number>());
}

function generatePoints(v1: number, v2: number, difference: number): number[] {
  return v1 === v2 ? [...new Array(difference)].fill(v1) : range(v1, v2);
}

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
