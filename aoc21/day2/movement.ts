export class Movement {
  direction: string;
  value: number;

  constructor(direction: string, value: number) {
    this.direction = direction;
    this.value = value;
  }
}

export function readCourse(rawMovements: string[]): Movement[] {
  return rawMovements.map((movement) => {
    const [direction, value] = movement.split(" ");
    return new Movement(direction, parseInt(value));
  });
}
