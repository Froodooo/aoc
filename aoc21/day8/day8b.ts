const input = await Deno.readTextFile("./day8/day8.txt");

function setSimpleNumbers(
  patternsMap: Map<number, string[]>,
  signalPatterns: string[][],
): void {
  for (let i = 0; i < signalPatterns.length; i++) {
    const pattern = signalPatterns[i];

    switch (pattern.length) {
      case 2:
        patternsMap.set(1, pattern);
        break;
      case 3:
        patternsMap.set(7, pattern);
        break;
      case 4:
        patternsMap.set(4, pattern);
        break;
      case 7:
        patternsMap.set(8, pattern);
        break;
    }
  }
}

function setLengthFiveNumbers(
  patternsMap: Map<number, string[]>,
  signalPatterns: string[][],
): void {
  for (let i = 0; i < signalPatterns.length; i++) {
    const pattern = signalPatterns[i];

    switch (pattern.length) {
      case 5: {
        if (patternsMap.get(1)?.every((p) => pattern.includes(p) ?? [])) {
          patternsMap.set(3, pattern);
        } else {
          const misses = (patternsMap.get(6) ?? []).reduce(
            (misses, p) => pattern.includes(p) ? misses : misses + 1,
            0,
          );
          if (misses === 1) patternsMap.set(5, pattern);
          else patternsMap.set(2, pattern);
        }
        break;
      }
    }
  }
}

function setLengthSixNumbers(
  patternsMap: Map<number, string[]>,
  signalPatterns: string[][],
): void {
  for (let i = 0; i < signalPatterns.length; i++) {
    const pattern = signalPatterns[i];

    switch (pattern.length) {
      case 6: {
        if (patternsMap.get(4)?.every((p) => pattern.includes(p)) ?? []) {
          patternsMap.set(9, pattern);
        } else if (
          patternsMap.get(1)?.every((p) => pattern.includes(p) ?? [])
        ) {
          patternsMap.set(0, pattern);
        } else patternsMap.set(6, pattern);
        break;
      }
    }
  }
}

function outputValueNumber(entry: string[][]): number {
  const [rawSignalPatterns, rawOutputValues] = entry;
  const signalPatterns = rawSignalPatterns.map((pattern) => pattern.split(""));
  const outputValues = rawOutputValues.map((pattern) => pattern.split(""));

  const patternsMap = new Map<number, string[]>();
  setSimpleNumbers(patternsMap, signalPatterns);
  setLengthSixNumbers(patternsMap, signalPatterns);
  setLengthFiveNumbers(patternsMap, signalPatterns);

  const patternsArray = Array.from(
    patternsMap,
    ([number, pattern]) => ({ number, pattern }),
  );

  const rawNumber = outputValues.map((values) => {
    return patternsArray.find(({ number: _, pattern: pattern }) =>
      values.length === pattern.length &&
      pattern.every((p) => values.includes(p))
    )?.number;
  }).join("");

  return parseInt(rawNumber);
}

export function solve(input: string): number {
  const lines = input.split("\n");
  const entries = lines.map((line) =>
    line.split(" | ").map((chunk) => chunk.split(" "))
  );
  const numbers = entries.map((entry) => outputValueNumber(entry));

  return numbers.reduce((total, number) => total + number, 0);
}

console.log(solve(input));
