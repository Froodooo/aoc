import { step } from "./common.ts";

const input = await Deno.readTextFile("./day20/day20.txt");

export function solve(input: string, enhancements: number): number {
  return step(input, enhancements);
}

console.log(solve(input, 50));
