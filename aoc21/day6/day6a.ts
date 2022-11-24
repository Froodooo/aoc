import { solve } from "./common.ts";

const input = await Deno.readTextFile("./day6/day6_ex.txt");
const result = solve(input, 80);
console.log(result);
