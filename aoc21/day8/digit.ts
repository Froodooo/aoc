export class Digit {
  value: number;
  segments: string[];
  digitLength: number;

  constructor(value: number, segments: string[]) {
    this.value = value;
    this.segments = segments;
    this.digitLength = segments.length;
  }

  updateSegments(segments: string[]) {
    this.segments = segments;
  }
}
