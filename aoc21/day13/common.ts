export class Coordinate {
  x: number;
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }

  fold(instruction: Instruction) {
    switch (instruction.axis) {
      case "x":
        if (this.x > instruction.value) {
          this.x = instruction.value - (this.x - instruction.value);
        }
        break;
      case "y":
        if (this.y > instruction.value) {
          this.y = instruction.value - (this.y - instruction.value);
        }
        break;
    }
  }

  exists(coordinates: Coordinate[]) {
    return coordinates.some((coordinate) =>
      this.x === coordinate.x && this.y === coordinate.y
    );
  }
}

export class Instruction {
  axis: string;
  value: number;

  constructor(axis: string, value: number) {
    this.axis = axis;
    this.value = value;
  }
}

export function readInstructions(rawInstructions: string): Instruction[] {
  return rawInstructions.split("\n").map((instruction) => {
    const [_, rawDirection] = instruction.split("fold along ");
    const [axis, value] = rawDirection.split("=");
    return new Instruction(axis, +value);
  });
}

export function readDots(rawDots: string): Coordinate[] {
  return rawDots.split("\n").map((dot) => {
    const [x, y] = dot.split(",");
    return new Coordinate(+x, +y);
  });
}

export function fold(
  coordinates: Coordinate[],
  instruction: Instruction,
): Coordinate[] {
  const emptyFoldedCoordinates: Coordinate[] = [];
  return coordinates.reduce((foldedCoordinates, coordinate) => {
    coordinate.fold(instruction);
    if (!coordinate.exists(foldedCoordinates)) {
      foldedCoordinates.push(coordinate);
    }
    return foldedCoordinates;
  }, emptyFoldedCoordinates);
}
