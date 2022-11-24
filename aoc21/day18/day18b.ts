import { add, readSnailfishNumber, reduce } from "./common.ts";

const input = await Deno.readTextFile("./day18/day18.txt");

export function solve(input: string): number {
  const lines = input.split("\n");

  let largestMagnitute = -1;

  for (let i = 0; i < lines.length; i++) {
    for (let j = 0; j < lines.length; j++) {
      if (i === j) continue;

      const root = add(
        readSnailfishNumber(lines[i]),
        readSnailfishNumber(lines[j]),
      );
      reduce(root);

      const magnitute = root.magnitude();
      largestMagnitute = magnitute > largestMagnitute
        ? magnitute
        : largestMagnitute;
    }
  }

  return largestMagnitute;
}

console.log(solve(input));
