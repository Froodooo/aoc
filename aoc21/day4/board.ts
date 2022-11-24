import { BoardNumber } from "./board_number.ts";

export class Board {
  numbers: BoardNumber[];
  won: boolean;

  constructor(numbers: BoardNumber[]) {
    this.numbers = numbers;
    this.won = false;
  }

  wins() {
    this.won = true;
  }
}
