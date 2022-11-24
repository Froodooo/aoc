import { solve } from "./common.ts";

const input = await Deno.readTextFile("./day7/day7.txt");

console.log(solve(input, { "isSummed": false }));
