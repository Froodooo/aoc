import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { Submarine } from "./day2b.ts";
import { Movement, readCourse } from "./movement.ts";

Deno.test("readCourse", () => {
  const rawMovements = ["forward 5"];
  assertEquals(
    readCourse(rawMovements),
    [new Movement("forward", 5)],
  );
});

Deno.test("move", () => {
  const movements: Movement[] = [
    new Movement("down", 5),
    new Movement("up", 2),
    new Movement("forward", 2),
  ];
  const submarine = new Submarine();
  movements.forEach((movement) => submarine.move(movement));
  assertEquals(submarine.horizontal_position, 2);
  assertEquals(submarine.aim, 3);
  assertEquals(submarine.depth, 6);
});

Deno.test("Example 1", async () => {
  const testInput = await Deno.readTextFile("./day2/day2_ex.txt");
  const movements = readCourse(testInput.split("\n"));
  const submarine = new Submarine();
  movements.forEach((movement) => submarine.move(movement));
  assertEquals(submarine.horizontal_position, 15);
  assertEquals(submarine.depth, 60);
});

Deno.test("Day 1", async () => {
  const testInput = await Deno.readTextFile("./day2/day2.txt");
  const movements = readCourse(testInput.split("\n"));
  const submarine = new Submarine();
  movements.forEach((movement) => submarine.move(movement));
  assertEquals(submarine.horizontal_position * submarine.depth, 2015547716);
});
