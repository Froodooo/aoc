const input = await Deno.readTextFile("./day21/day21.txt");

const memoized = new Map<string, number[]>();

function play(
  player1: number,
  player2: number,
  score1: number,
  score2: number,
): number[] {
  if (score1 >= 21) {
    return [1, 0];
  }

  if (score2 >= 21) {
    return [0, 1];
  }

  const key = `${player1},${player2},${score1},${score2}`;

  if (memoized.has(key)) return memoized.get(key)!;

  const scores = [0, 0];

  for (const die1 of [1, 2, 3]) {
    for (const die2 of [1, 2, 3]) {
      for (const die3 of [1, 2, 3]) {
        let newPosition = player1 + die1 + die2 + die3;
        newPosition = newPosition % 10 === 0 ? 10 : newPosition % 10;
        const newScore = score1 + newPosition;

        const winner = play(player2, newPosition, score2, newScore);

        scores[0] += winner[1];
        scores[1] += winner[0];
      }
    }
  }

  memoized.set(key, scores);

  return scores;
}

function readGame(input: string): number[] {
  return input.split("\n").reduce((acc: number[], line) => {
    const [_, _id, position] = line.match(
      /^Player (\d+) starting position: (\d+)$/,
    )!;
    acc.push(+position);
    return acc;
  }, []);
}

export function solve(input: string): number {
  const [player1, player2] = readGame(input);

  const result = play(player1, player2, 0, 0);

  return Math.max(...result);
}

console.log(solve(input));
