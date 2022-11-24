import { Bingo } from "./bingo.ts";
import { Board } from "./board.ts";
import { BoardNumber } from "./board_number.ts";
import { chunked } from "https://deno.land/std@0.106.0/collections/chunked.ts";

export function readDraw(input: string): number[] {
  return input.split("\n")[0].split(",").map((number) => parseInt(number));
}

export function readBoards(input: string): Board[] {
  const lines = input.split("\n").filter((line) => line != "");
  const rawBoards = chunked(lines.slice(1), 5)
    .map((rawBoard) => {
      const boardNumbers = [];
      for (let i = 0; i < 5; i++) {
        const boardLine = rawBoard[i].split(" ").filter((number) =>
          number != ""
        );
        for (let j = 0; j < 5; j++) {
          boardNumbers.push(
            new BoardNumber(parseInt(boardLine[j].trim()), j, i),
          );
        }
      }
      return boardNumbers;
    });

  return rawBoards.map((boardNumbers) => new Board(boardNumbers));
}

export function calculateResult(bingo: Bingo): number | undefined {
  if (bingo.lastWinner) {
    const sumUnmarked = bingo.lastWinner.numbers.filter((number) =>
      !number.marked
    )
      .map((number) => number.value).reduce((sum, current) => sum + current, 0);
    const lastDraw = bingo.lastDraw;
    return sumUnmarked * lastDraw;
  }
}
