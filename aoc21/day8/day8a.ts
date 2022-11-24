import { Digit } from "./digit.ts";

const input = await Deno.readTextFile("./day8/day8.txt");

const digits: Digit[] = [
  new Digit(0, ["a", "b", "c", "e", "f", "g"]),
  new Digit(1, ["c", "f"]),
  new Digit(2, ["a", "c", "d", "e", "g"]),
  new Digit(3, ["a", "c", "d", "f", "g"]),
  new Digit(4, ["b", "c", "d", "f"]),
  new Digit(5, ["a", "b", "d", "f", "g"]),
  new Digit(6, ["a", "b", "d", "e", "f", "g"]),
  new Digit(7, ["a", "c", "f"]),
  new Digit(8, ["a", "b", "c", "d", "e", "f", "g"]),
  new Digit(9, ["a", "b", "c", "d", "f", "g"]),
];

const simpleDigits = digits.filter((digit) =>
  [1, 4, 7, 8].includes(digit.value)
);

function numberOfSimpleDigits(outputValues: string[][]): number {
  const simpleDigitsLengths = simpleDigits.map((simpleDigit) =>
    simpleDigit.digitLength
  );
  return outputValues.reduce((outputValueCount, fourDigitOutputValue) => {
    return outputValueCount +
      fourDigitOutputValue.reduce((count, digitOutputValue) => {
        return count +
          (simpleDigitsLengths.includes(digitOutputValue.length) ? 1 : 0);
      }, 0);
  }, 0);
}

export function solve(input: string): number {
  const lines = input.split("\n");
  const entries = lines.map((line) => line.split(" | "));
  const rawOutputValues = entries.map(([_, outputValue]) => outputValue);
  const outputValues = rawOutputValues.map((outputValue) =>
    outputValue.split(" ")
  );

  return numberOfSimpleDigits(outputValues);
}

console.log(solve(input));
