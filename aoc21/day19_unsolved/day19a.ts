import { permutations } from "https://deno.land/std@0.118.0/collections/mod.ts";

const input = await Deno.readTextFile("./day19/day19_ex.txt");

class Coordinate {
  x: number;
  y: number;
  z: number;

  constructor(x: number, y: number, z: number) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  orientations(): Coordinate[] {
    const rotations = permutations([this.x, this.y, this.z]).map(([x, y, z]) =>
      new Coordinate(x, y, z)
    );
    const facings = [[1, 1], [1, -1], [-1, 1], [-1, -1]];

    const orientations = [];
    for (const rotation of rotations) {
      for (const facing of facings) {
        orientations.push(
          new Coordinate(
            rotation.x * facing[0],
            rotation.y * facing[1],
            rotation.z,
          ),
        );
      }
    }

    return orientations;
  }
}

class Scanner {
  id: number;
  beaconPositions: Coordinate[];

  constructor(id: number, beaconPositions: Coordinate[]) {
    this.id = id;
    this.beaconPositions = beaconPositions;
  }

  compare(scanner: Scanner) {
    const map = new Map<string, number>();

    for (const thisCoordinate of this.beaconPositions) {
      for (const scannerCoordinate of scanner.beaconPositions) {
        for (const orientation of scannerCoordinate.orientations()) {
          const [dx, dy, dz] = [
            orientation.x - thisCoordinate.x,
            orientation.y - thisCoordinate.y,
            orientation.z - thisCoordinate.z,
          ];

          const key = `${dx},${dy},${dz}`;
          const value = map.get(key) ?? 0;
          map.set(key, value + 1);
        }
      }
    }

    // const result = Array.from(map).filter(([_, value]) => value >= 2);
    // return;
  }
}

function readScanners(input: string): Scanner[] {
  return input.split("\n\n").map((scanner) => {
    const scannerLines = scanner.split("\n");
    const header = scannerLines.splice(0, 1)[0];
    const id = +header.match(/--- scanner (\d) ---/)![1];
    const coordinates = scannerLines.map((line) => {
      const [x, y, z] = line.split(",");
      return new Coordinate(+x, +y, +z);
    });

    return new Scanner(id, coordinates);
  });
}

function solve(input: string): number {
  const scanners = readScanners(input);

  scanners[0].compare(scanners[1]);

  // const orientations = scanners[0].beaconPositions[4].orientations();
  // console.log(scanners[0].beaconPositions[4].orientations());
  // console.log(permutations(["x", "y", "z"]));
  // console.log(scanners)
  return 42;
}

solve(input);
