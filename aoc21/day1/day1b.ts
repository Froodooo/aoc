import { slidingWindows } from "https://deno.land/std@0.116.0/collections/sliding_windows.ts";
import { sumOf } from "https://deno.land/std@0.116.0/collections/sum_of.ts";

export function countIncreases(measurements: number[]): number {
  return slidingWindows(measurements, 3).reduce((acc, currentWindow) => {
    const currentSum = sumOf(currentWindow, (m) => m);
    if (currentSum > acc.previousSum) {
      acc.increases++;
    }
    acc.previousSum = currentSum;
    return acc;
  }, { previousSum: Infinity, increases: 0 }).increases;
}

const input = await Deno.readTextFile("./day1/day1.txt");
const measurements = input.split("\n").map((measurement) =>
  parseInt(measurement)
);

console.log(countIncreases(measurements));
