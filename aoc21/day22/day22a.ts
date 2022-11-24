const input = await Deno.readTextFile("./day22/day22.txt");

class Step {
  mode: string;
  x: number[];
  y: number[];
  z: number[];

  constructor(step: string) {
    const [mode, rawCuboid] = step.split(" ");
    const [x, y, z] = rawCuboid.split(",");
    const [xStart, xEnd] = x.replace("x=", "").split("..").map(Number);
    const [yStart, yEnd] = y.replace("y=", "").split("..").map(Number);
    const [zStart, zEnd] = z.replace("z=", "").split("..").map(Number);

    this.mode = mode;
    this.x = range(xStart, xEnd);
    this.y = range(yStart, yEnd);
    this.z = range(zStart, zEnd);
  }
}

// https://stackoverflow.com/a/15453499
function range(start: number, stop: number, step = 1) {
  const a = [start];
  let b = start;
  while (b < stop) {
    a.push(b += step || 1);
  }
  return a;
}

function isInRange(x: number[], y: number[], z: number[]): boolean {
  const validRange = range(-50, 50);
  return validRange.includes(x[0]) && validRange.includes(x[x.length - 1]) &&
    validRange.includes(y[0]) && validRange.includes(y[y.length - 1]) &&
    validRange.includes(z[0]) && validRange.includes(z[z.length - 1]);
}

function doStep(step: Step, onCubes: Set<string>): Set<string> {
  if (!isInRange(step.x, step.y, step.z)) {
    return onCubes;
  }

  for (let x = step.x[0]; x <= step.x[step.x.length - 1]; x++) {
    for (let y = step.y[0]; y <= step.y[step.y.length - 1]; y++) {
      for (let z = step.z[0]; z <= step.z[step.z.length - 1]; z++) {
        const key = `${x},${y},${z}`;

        switch (step.mode) {
          case "on":
            onCubes.add(key);
            break;
          case "off":
            onCubes.delete(key);
            break;
          default:
            throw new Error("Unknown mode");
        }
      }
    }
  }
  return onCubes;
}

function getSteps(input: string) {
  return input.split("\n").map((step) => new Step(step));
}

export function solve(input: string): number {
  let onCubes = new Set<string>();
  const steps = getSteps(input);

  for (const step of steps) {
    onCubes = doStep(step, onCubes);
  }

  return onCubes.size;
}

console.log(solve(input));
