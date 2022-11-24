export class Point {
  x: number;
  y: number;
  value: number;

  constructor(x: number, y: number, value: number) {
    this.x = x;
    this.y = y;
    this.value = value;
  }

  isSame(point: Point) {
    return this.x === point.x && this.y === point.y;
  }

  isLower(point: Point) {
    return this.x < point.x || this.y < point.y;
  }

  isHigher(point: Point) {
    return this.x > point.x || this.y > point.y;
  }

  isOption(point: Point) {
    return this.value > point.value;
  }

  withinMap(map: number[][]) {
    return this.y < map.length && this.x < map[0].length && this.y >= 0 &&
      this.x >= 0;
  }

  setValue(map: number[][]) {
    this.value = map[this.y][this.x];
  }

  inBasin(basins: Point[][]) {
    return basins.some((basin) => {
      return basin.some((point) => this.isSame(point));
    });
  }
}
