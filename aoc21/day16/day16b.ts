import {
  LITERAL_TYPE_ID,
  OperatorPacket,
  Packet,
  solvePart,
} from "./common.ts";

function getSum(packet: Packet, sum: number): number {
  if (packet.typeId === LITERAL_TYPE_ID) {
    return packet.value;
  }

  const operatorPacket = packet as OperatorPacket;
  switch (packet.typeId) {
    case 0: {
      return operatorPacket.subPackets.reduce(
        (acc, subPacket) => acc + getSum(subPacket, acc),
        0,
      );
    }
    case 1: {
      return operatorPacket.subPackets.reduce(
        (acc, subPacket) => acc * getSum(subPacket, acc),
        1,
      );
    }
    case 2: {
      return Math.min(
        ...operatorPacket.subPackets.map((subPacket) => getSum(subPacket, 0)),
      );
    }
    case 3: {
      return Math.max(
        ...operatorPacket.subPackets.map((subPacket) => getSum(subPacket, 0)),
      );
    }
    case 5: {
      const greatherThan = operatorPacket.subPackets.map((subPacket) =>
        getSum(subPacket, 0)
      );
      return greatherThan[0] > greatherThan[1] ? 1 : 0;
    }
    case 6: {
      const smallerThan = operatorPacket.subPackets.map((subPacket) =>
        getSum(subPacket, 0)
      );
      return smallerThan[0] < smallerThan[1] ? 1 : 0;
    }
    case 7: {
      const equal = operatorPacket.subPackets.map((subPacket) =>
        getSum(subPacket, 0)
      );
      return equal[0] === equal[1] ? 1 : 0;
    }
    default: {
      return sum;
    }
  }
}

export function solve(input: string): number {
  const packet = solvePart(input);

  return getSum(packet, 0);
}

const input = await Deno.readTextFile("./day16/day16.txt");
console.log(solve(input));
