// import { fetchInputData, writeInputData } from "../utilities.ts";
export function countIncreases(measurements: number[]): number {
  let increases = 0;

  for (let i = 1; i < measurements.length; i++) {
    increases = measurements[i] > measurements[i - 1]
      ? increases + 1
      : increases;
  }

  return increases;
}

const input = await Deno.readTextFile("./day1/day1.txt");
const measurements = input.split("\n").map((measurement) =>
  parseInt(measurement)
);

console.log(countIncreases(measurements));
