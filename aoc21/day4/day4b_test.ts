import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { readBoards, readDraw } from "./common.ts";
import { Bingo } from "./bingo.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day4/day4_ex.txt");
  const draw = readDraw(input);
  const boards = readBoards(input);
  const bingo = new Bingo(boards, draw);

  bingo.play(true);

  if (bingo.lastWinner) {
    const sumUnmarked = bingo.lastWinner.numbers.filter((number) =>
      !number.marked
    )
      .map((number) => number.value).reduce((sum, current) => sum + current, 0);
    const lastDraw = bingo.lastDraw;

    assertEquals(sumUnmarked * lastDraw, 1924);
  }
});

Deno.test("Day 4", async () => {
  const input = await Deno.readTextFile("./day4/day4.txt");
  const draw = readDraw(input);
  const boards = readBoards(input);
  const bingo = new Bingo(boards, draw);

  bingo.play(true);

  if (bingo.lastWinner) {
    const sumUnmarked = bingo.lastWinner.numbers.filter((number) =>
      !number.marked
    )
      .map((number) => number.value).reduce((sum, current) => sum + current, 0);
    const lastDraw = bingo.lastDraw;

    assertEquals(sumUnmarked * lastDraw, 9576);
  }
});
