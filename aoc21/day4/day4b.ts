import { Bingo } from "./bingo.ts";
import { calculateResult, readBoards, readDraw } from "./common.ts";

const input = await Deno.readTextFile("./day4/day4.txt");
const draw = readDraw(input);
const boards = readBoards(input);
const bingo = new Bingo(boards, draw);

bingo.play(true);
console.log(calculateResult(bingo));
