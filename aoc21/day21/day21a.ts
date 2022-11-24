const input = await Deno.readTextFile("./day21/day21.txt");

enum DieType {
  Deterministic,
}

interface Die {
  position: number;
  rolls: number;

  roll(): number[];
}

class DeterministicDie implements Die {
  position: number;
  rolls = 0;

  constructor(position: number) {
    this.position = position;
  }

  roll(): number[] {
    const numbers = [];

    for (let i = 0; i < 3; i++) {
      numbers.push(this.position);
      this.position += 1;
      if (this.position === 101) {
        this.position = 1;
      }
      this.rolls += 1;
    }

    return numbers;
  }
}

class Game {
  players: Player[];
  die: Die;
  finished = false;

  constructor(players: Player[], dieType: DieType) {
    this.players = players;

    switch (dieType) {
      case DieType.Deterministic:
        this.die = new DeterministicDie(1);
        break;
      default:
        throw new Error("Unknown die type");
    }
  }

  play(): void {
    while (!this.finished) {
      for (let i = 0; i < this.players.length; i++) {
        this.players[i].roll(this.die);
        if (this.players[i].isFinished()) {
          this.finished = true;
          break;
        }
      }
    }
  }

  getLosers(): Player[] {
    return this.players.filter((player) => player.score < 1000);
  }
}

class Player {
  id: number;
  position: number;
  score = 0;

  constructor(id: number, position: number) {
    this.id = id;
    this.position = position;
  }

  roll(die: Die): void {
    const rolls = die.roll();
    const totalRoll = rolls.reduce((a, b) => a + b, 0);
    this.position = this.position + totalRoll;
    this.position = this.position % 10 === 0 ? 10 : this.position % 10;
    this.score += this.position;
  }

  isFinished(): boolean {
    return this.score >= 1000;
  }
}

function readPlayer(input: string): Player {
  const [_, id, position] = input.match(
    /^Player (\d+) starting position: (\d+)$/,
  )!.map(Number);
  return new Player(id, position);
}

function readPlayers(input: string): Player[] {
  return input.split("\n").map((line) => readPlayer(line));
}

export function solve(input: string): number {
  const players = readPlayers(input);

  const game = new Game(players, DieType.Deterministic);
  game.play();

  return game.getLosers()[0].score * game.die.rolls;
}

console.log(solve(input));
