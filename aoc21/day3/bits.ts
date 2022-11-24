export function countBits(binaryNumbers: string[]): number[] {
  const positions = new Array(binaryNumbers[0].length).fill(0);

  binaryNumbers.forEach((binary) => {
    let number = parseInt(binary, 2);
    let index = 0;
    while (number != 0) {
      if ((number & 1) == 1) {
        positions[index] = positions[index] + 1;
      }

      number = number >> 1;
      index += 1;
    }
  });

  positions.reverse();
  return positions;
}
