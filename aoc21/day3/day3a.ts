import { countBits } from "./bits.ts";

export function gamma(positions: number[], total: number): number {
  const binary = positions.map((numberOfOnes) => {
    return numberOfOnes > total / 2 ? "1" : "0";
  }).join("");

  const number = parseInt(binary, 2);

  return number;
}

export function epsilon(positions: number[], total: number): number {
  const binary = positions.map((numberOfOnes) => {
    return numberOfOnes > total / 2 ? "0" : "1";
  }).join("");

  const number = parseInt(binary, 2);

  return number;
}

const input = await Deno.readTextFile("./day3/day3.txt");
const binaries = input.split("\n");
const positions = countBits(binaries);
const gammaNumber = gamma(positions, binaries.length);
const epsilonNumber = epsilon(positions, binaries.length);

console.log(gammaNumber * epsilonNumber);
