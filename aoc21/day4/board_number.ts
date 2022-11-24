export class BoardNumber {
  value: number;
  x: number;
  y: number;
  marked: boolean;

  constructor(value: number, x: number, y: number) {
    this.value = value;
    this.x = x;
    this.y = y;
    this.marked = false;
  }

  mark() {
    this.marked = true;
  }
}
