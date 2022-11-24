const input = await Deno.readTextFile("./day13/day13.txt");
import { Coordinate, fold, readDots, readInstructions } from "./common.ts";

function print(dots: Coordinate[]) {
  const maxX = Math.max(...dots.map((dot) => dot.x)) + 1;
  const maxY = Math.max(...dots.map((dot) => dot.y)) + 1;

  for (let y = 0; y < maxY; y++) {
    let line = "";
    for (let x = 0; x < maxX; x++) {
      const coordinate = new Coordinate(x, y);
      line += coordinate.exists(dots) ? "█" : " ";
    }
    console.log(line);
  }
}

export function solve(input: string): void {
  const [rawDots, rawInstructions] = input.split("\n\n");
  const dots = readDots(rawDots);
  const instructions = readInstructions(rawInstructions);

  const initialCoordinates = [...dots];
  const resultDots = instructions.reduce((foldedCoordinates, instruction) => {
    return fold(foldedCoordinates, instruction);
  }, initialCoordinates);

  print(resultDots);
}

solve(input);
