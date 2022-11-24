type dimensions = { minX: number; minY: number; maxX: number; maxY: number };

const squareDelta = [
  [-1, -1],
  [0, -1],
  [1, -1],
  [-1, 0],
  [0, 0],
  [1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
];

function getSquareNumber(
  [x, y]: number[],
  lightPixels: Set<string>,
  allLightsOn: boolean,
) {
  const binaryArray = squareDelta.reduce((binary, [dx, dy]) => {
    const [neighbourX, neighbourY] = [x + dx, y + dy];

    binary.push(
      lightPixels.has(`${neighbourX},${neighbourY}`) !== allLightsOn ? 1 : 0,
    );
    return binary;
  }, []);

  const binary = binaryArray.join("");
  return parseInt(binary, 2);
}

export function getDimensions(lightPixels: Set<string>): dimensions {
  const inputImage = Array.from(lightPixels).map((point) =>
    point.split(",").map(Number)
  );

  const minX = inputImage.reduce((max, [x]) => Math.min(max, x), 0) - 200;
  const minY = inputImage.reduce((max, [, y]) => Math.min(max, y), 0) - 200;
  const maxX = inputImage.reduce((max, [x]) => Math.max(max, x), 0) + 200;
  const maxY = inputImage.reduce((max, [, y]) => Math.max(max, y), 0) + 200;

  return { minX, minY, maxX, maxY };
}

export function updateDimensions(
  { minX: minX, minY: minY, maxX: maxX, maxY: maxY }: dimensions,
): dimensions {
  return { minX: minX + 3, minY: minY + 3, maxX: maxX - 3, maxY: maxY - 3 };
}

export function readLightPixels([_, section]: string[]): Set<string> {
  const lightPixels = new Set<string>();

  const pixelLines = section.split("\n");
  for (let y = 0; y < pixelLines.length; y++) {
    const pixels = pixelLines[y].split("");
    for (let x = 0; x < pixels.length; x++) {
      if (pixels[x] === "#") {
        lightPixels.add(`${x},${y}`);
      }
    }
  }

  return lightPixels;
}

export function readImageEnhancementAlgorithm(
  [section, _]: string[],
): string[] {
  return section.split("");
}

export function enhance(
  lightPixels: Set<string>,
  algorithm: string[],
  allLightsOn: boolean,
): Set<string> {
  const { minX, minY, maxX, maxY } = getDimensions(lightPixels);

  const newLightPixels = new Set<string>();

  for (let y = minY - 1; y <= maxY + 1; y++) {
    for (let x = minX - 1; x <= maxX + 1; x++) {
      const squareNumber = getSquareNumber([x, y], lightPixels, allLightsOn);
      if (algorithm[squareNumber] === "#" === allLightsOn) {
        newLightPixels.add(`${x},${y}`);
      }
    }
  }

  return newLightPixels;
}

export function step(input: string, enhancements: number): number {
  const sections = input.split("\n\n");

  const imageEnhancementAlgorithm = readImageEnhancementAlgorithm(sections);
  let lightPixels = readLightPixels(sections);

  for (let i = 0; i < enhancements; i++) {
    lightPixels = enhance(
      new Set(Array.from(lightPixels)),
      imageEnhancementAlgorithm,
      i % 2 === 1, // all lights on in uneven steps
    );
  }

  return lightPixels.size;
}
