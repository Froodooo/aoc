import { Board } from "./board.ts";
import { chunked } from "https://deno.land/std@0.106.0/collections/chunked.ts";

export class Bingo {
  boards: Board[];
  draw: number[];
  lastDraw: number;
  lastWinner: Board | undefined;
  numberOfWinners: number;

  constructor(boards: Board[], draw: number[]) {
    this.boards = boards;
    this.draw = draw;
    this.lastDraw = -1;
    this.lastWinner = undefined;
    this.numberOfWinners = 0;
  }

  play(untilLast = false) {
    let drawIndex = 0;
    let finished = false;
    while (!finished || drawIndex == this.draw.length) {
      this.lastDraw = this.draw[drawIndex];
      for (const board of this.boards) {
        this.sortBoardRows(board);
        for (const number of board.numbers) {
          if (number.value == this.lastDraw) {
            number.mark();
          }
        }

        if (!board.won && this.checkWinner(board)) {
          this.handleWin(board);
        }

        this.sortBoardColumns(board);
        if (!board.won && this.checkWinner(board)) {
          this.handleWin(board);
        }
      }

      drawIndex += 1;
      finished = this.isFinished(untilLast);
    }
  }

  private isFinished(untilLast: boolean): boolean {
    if (untilLast) {
      return this.numberOfWinners == this.boards.length;
    } else {
      return this.lastWinner != undefined;
    }
  }

  private handleWin(board: Board): void {
    board.wins();
    this.lastWinner = board;
    this.numberOfWinners += 1;
  }

  private sortBoardRows(board: Board): void {
    board.numbers.sort((number1, number2) =>
      number1.y < number2.y ? -1 : number1.y > number2.y ? 1 : 0
    );
  }

  private sortBoardColumns(board: Board): void {
    board.numbers.sort((number1, number2) =>
      number1.x < number2.x ? -1 : number1.x > number2.x ? 1 : 0
    );
  }

  private checkWinner(board: Board): boolean {
    for (const chunk of chunked(board.numbers, 5)) {
      if (chunk.every((number) => number.marked)) {
        return true;
      }
    }

    return false;
  }
}
