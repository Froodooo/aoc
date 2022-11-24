const INTERVAL = 6;
const MAX_INTERVAL = 8;

export function solve(input: string, days: number): number {
  const fish = readFish(input);

  for (let _i = 0; _i < days; _i++) {
    const zeroTimerFish = getZeroTimerFish(fish);

    updateTimers(fish);
    resetFishTimers(fish, zeroTimerFish);
    addFish(fish, zeroTimerFish);
  }

  return fish.reduce((a, b) => a + b);
}

function getZeroTimerFish(fish: number[]): number {
  return fish[0];
}

function updateTimers(fish: number[]): void {
  for (let j = 0; j < fish.length - 1; j++) {
    fish[j] = fish[j + 1];
  }
}

function resetFishTimers(fish: number[], zeroTimerFish: number): void {
  fish[INTERVAL] += zeroTimerFish;
}

function addFish(fish: number[], zeroTimerFish: number): void {
  fish[fish.length - 1] = zeroTimerFish;
}

function readFish(input: string): number[] {
  return input.split(",").map((f) => parseInt(f)).reduce(
    (fishTimers, f) => {
      fishTimers[f] += 1;
      return fishTimers;
    },
    new Array(MAX_INTERVAL + 1).fill(0),
  );
}
