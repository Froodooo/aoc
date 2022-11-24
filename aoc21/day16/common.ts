let transmission: string[];

export const LITERAL_TYPE_ID = 4;

export enum Type {
  Literal,
  Operator,
}

enum LengthType {
  Zero,
  One,
  None,
}

export class Packet {
  version: number;
  typeId: number;
  type: Type;
  value: number;
  bits: string[];

  constructor(version: string[], typeId: string[]) {
    this.version = parseInt(version.join(""), 2);
    this.typeId = parseInt(typeId.join(""), 2);
    this.type = this.typeId === LITERAL_TYPE_ID ? Type.Literal : Type.Operator;
    this.value = 0;
    this.bits = version.concat(typeId);
  }
}

class LiteralPacket extends Packet {
  constructor(version: string[], typeId: string[]) {
    super(version, typeId);

    this.value = this.readLiteralPacket();
  }

  private readLiteralPacket(): number {
    let group: string[];
    let groupBits = "";

    do {
      group = transmission.splice(0, 5);
      groupBits += group.slice(1).join("");
      this.bits = this.bits.concat(group);
    } while (group[0] == "1");

    const literal = parseInt(groupBits, 2);

    return literal;
  }
}

export class OperatorPacket extends Packet {
  lengthType: LengthType;
  length: number;
  subPackets: Packet[];

  constructor(version: string[], typeId: string[]) {
    super(version, typeId);

    this.lengthType = LengthType.None;
    this.length = 0;
    this.subPackets = [];

    this.readOperatorPacket();
  }

  private readOperatorPacket() {
    const lengthType = transmission.splice(0, 1)[0];
    this.bits.push(lengthType);
    this.lengthType = lengthType == "0" ? LengthType.Zero : LengthType.One;

    let length;
    switch (this.lengthType) {
      case LengthType.Zero:
        length = transmission.splice(0, 15);
        this.bits = this.bits.concat(length);
        this.length = parseInt(length.join(""), 2);
        this.readInternalSubPackets();
        break;
      case LengthType.One:
        length = transmission.splice(0, 11);
        this.bits = this.bits.concat(length);
        this.length = parseInt(length.join(""), 2);
        this.readExternalSubPackets();
        break;
    }
  }

  private readExternalSubPackets() {
    for (let i = 0; i < this.length; i++) {
      const packet = readPacket();
      this.subPackets.push(packet);
      this.bits = this.bits.concat(packet.bits);
    }
  }

  private readInternalSubPackets() {
    let subPacketCount = 0;

    while (subPacketCount !== this.length) {
      const packet = readPacket();
      this.subPackets.push(packet);
      subPacketCount += packet.bits.length;
      this.bits = this.bits.concat(packet.bits);
    }
  }
}

// https://stackoverflow.com/questions/45053624/convert-hex-to-binary-in-javascript
function hex2bin(hex: string): string {
  return (parseInt(hex, 16).toString(2)).padStart(4, "0");
}

function toBinary(hex: string): string {
  return hex.split("").map((h) => hex2bin(h)).join("");
}

function readPacket(): Packet {
  const version = transmission.splice(0, 3);
  const typeId = transmission.splice(0, 3);
  const packet = new Packet(version, typeId);

  switch (packet.type) {
    case Type.Literal:
      return new LiteralPacket(version, typeId);
    case Type.Operator:
      return new OperatorPacket(version, typeId);
    default:
      throw new Error("Unknown packet type");
  }
}

export function solvePart(input: string): Packet {
  transmission = toBinary(input).split("");
  return readPacket();
}
