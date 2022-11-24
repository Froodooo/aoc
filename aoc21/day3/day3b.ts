import { countBits } from "./bits.ts";

export function oxygen(
  binaryNumbers: string[],
): number {
  let index = 0;
  let onePositionsCount = [];

  while (binaryNumbers.length > 1) {
    onePositionsCount = countBits(binaryNumbers);
    const bit = onePositionsCount[index] >= binaryNumbers.length / 2
      ? "1"
      : "0";
    binaryNumbers = binaryNumbers.filter((binary) =>
      binary.charAt(index) == bit
    );

    index += 1;
  }

  return parseInt(binaryNumbers[0], 2);
}

export function co2Scrubber(
  binaryNumbers: string[],
): number {
  let index = 0;
  let onePositionsCount = [];

  while (binaryNumbers.length > 1) {
    onePositionsCount = countBits(binaryNumbers);
    const bit = onePositionsCount[index] >= binaryNumbers.length / 2
      ? "0"
      : "1";
    binaryNumbers = binaryNumbers.filter((binary) =>
      binary.charAt(index) == bit
    );

    index += 1;
  }

  return parseInt(binaryNumbers[0], 2);
}

const input = await Deno.readTextFile("./day3/day3.txt");

const binaries = input.split("\n");
const oxygenNumber = oxygen(binaries);
const co2ScrubberNumber = co2Scrubber(binaries);

console.log(oxygenNumber * co2ScrubberNumber);
