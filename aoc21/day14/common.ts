import { frequencies } from "https://deno.land/x/pine@0.5.0/frequencies.ts";
import { slidingWindows } from "https://deno.land/std@0.108.0/collections/mod.ts";

type rules = Map<string, string>;
type pairs = Map<string, number>;

function readRules(input: string): rules {
  return input.split("\n").reduce((rules, line) => {
    const [pair, insertion] = line.split(" -> ");
    rules.set(pair, insertion);
    return rules;
  }, new Map<string, string>());
}

function stepPairCount(
  pairCount: pairs,
  pair: string,
  count: number,
  letter: string,
) {
  const splitPair = pair.split("");
  const newPairs = [splitPair[0] + letter, letter + splitPair[1]];
  newPairs.forEach((newPair) => {
    const currentSize = pairCount.get(newPair) ?? 0;
    pairCount.set(newPair, currentSize + count);
  });

  return pairCount;
}

function stepLetterCount(
  letterCount: pairs,
  letter: string,
  count: number,
): pairs {
  const currentLetterSize = letterCount.get(letter) ?? 0;
  letterCount.set(letter, currentLetterSize + count);
  return letterCount;
}

function step(
  pairCount: pairs,
  letterCount: pairs,
  rules: rules,
): [pairs, pairs] {
  let newPairCount = new Map<string, number>();
  for (const [pair, count] of Array.from(pairCount.entries())) {
    const letter = rules.get(pair) ?? "";

    letterCount = stepLetterCount(letterCount, letter, count);
    newPairCount = stepPairCount(newPairCount, pair, count, letter);
  }
  return [newPairCount, letterCount];
}

function gePairCount(polymer: string): pairs {
  const pairs = slidingWindows(polymer.split(""), 2);
  return pairs.reduce((pairCount, pair) => {
    const joinedPair = pair.join("");
    const currentSize = pairCount.get(joinedPair) ?? 0;
    pairCount.set(joinedPair, currentSize + 1);
    return pairCount;
  }, new Map<string, number>());
}

function getLetterCount(polymer: string): pairs {
  return frequencies(polymer.split(""));
}

export function run(input: string, iterations: number): number {
  const [polymer, rawRules] = input.split("\n\n");
  const rules = readRules(rawRules);

  let pairCount = gePairCount(polymer);
  let letterCount = getLetterCount(polymer);

  for (let i = 0; i < iterations; i++) {
    [pairCount, letterCount] = step(pairCount, letterCount, rules);
  }

  const values = Array.from(letterCount.values()).sort((a, b) => a - b);
  return values[values.length - 1] - values[0];
}
