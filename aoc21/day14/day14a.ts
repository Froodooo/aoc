import { run } from "./common.ts";
const input = await Deno.readTextFile("./day14/day14.txt");

export function solve(input: string): number {
  return run(input, 10);
}

console.log(solve(input));
