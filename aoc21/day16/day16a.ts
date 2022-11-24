import { OperatorPacket, Packet, solvePart, Type } from "./common.ts";

function versionSum(packet: Packet, sum: number): number {
  sum += packet.version;

  if (packet.type === Type.Operator) {
    const operatorPacket = packet as OperatorPacket;
    sum += operatorPacket.subPackets.reduce((acc, subPacket) => {
      acc += versionSum(subPacket, 0);
      return acc;
    }, 0);
  }

  return sum;
}

export function solve(input: string): number {
  const packet = solvePart(input);

  return versionSum(packet, 0);
}

const input = await Deno.readTextFile("./day16/day16.txt");
console.log(solve(input));
