import { add, readSnailfishNumbers, reduce } from "./common.ts";

const input = await Deno.readTextFile("./day18/day18.txt");

export function solve(input: string): number {
  const trees = readSnailfishNumbers(input);

  let root = trees[0];
  for (let i = 1; i < trees.length; i++) {
    root = add(root, trees[i]);
    reduce(root);
  }

  return root.magnitude();
}

console.log(solve(input));
