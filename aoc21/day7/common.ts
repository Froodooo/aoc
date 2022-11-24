type SolveOptions = { isSummed: boolean };

export function solve(input: string, options: SolveOptions): number {
  const positions = input.split(",").map((position) => parseInt(position));
  const fuel = range(positions).reduce((minFuel, positionToCheck) => {
    const fuelToCheck = positions.reduce(
      (totalFuel, position) => {
        return fuelSum(totalFuel, position, positionToCheck, options);
      },
      0,
    );
    return fuelToCheck < minFuel ? fuelToCheck : minFuel;
  }, Infinity);

  return fuel;
}

function range(positions: number[]): number[] {
  return Array.from({
    length: Math.max(...positions) - Math.min(...positions) + 1,
  }, (_, i) => i);
}

function fuelSum(
  totalFuel: number,
  position: number,
  positionToCheck: number,
  options: SolveOptions,
): number {
  return options.isSummed
    ? summedFuel(totalFuel, position, positionToCheck)
    : normalFuel(totalFuel, position, positionToCheck);
}

function normalFuel(
  totalFuel: number,
  position: number,
  positionToCheck: number,
): number {
  return totalFuel + Math.abs(positionToCheck - position);
}

function summedFuel(
  totalFuel: number,
  position: number,
  positionToCheck: number,
): number {
  const distance = Math.abs(positionToCheck - position);
  const positionFuel = (distance * (distance + 1)) / 2;
  return totalFuel + positionFuel;
}
