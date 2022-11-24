type SnailfishNumber = number | number[] | SnailfishNumber[];

export class Node {
  id: string;
  parent: Node | undefined;
  left: Node | undefined;
  right: Node | undefined;
  value: number | undefined;

  constructor() {
    this.id = crypto.randomUUID();
  }

  toString(): string {
    if (Number.isInteger(this.value)) {
      return `${this.value}`;
    }
    return `[${this.left?.toString()},${this.right?.toString()}]`;
  }

  magnitude(): number {
    if (Number.isInteger(this.value)) {
      return this.value!;
    }
    return 3 * this.left?.magnitude()! + 2 * this.right?.magnitude()!;
  }
}

export function buildTree(snailfishNumber: SnailfishNumber): Node {
  const root = new Node();

  if (Number.isInteger(snailfishNumber)) {
    root.value = snailfishNumber as unknown as number;
    return root;
  }

  const [left, right] = snailfishNumber as number[][][][];
  root.left = buildTree(left);
  root.right = buildTree(right);

  root.left.parent = root;
  root.right.parent = root;

  return root;
}

export function readSnailfishNumbers(input: string): Node[] {
  return input.split("\n").map((line) => eval(line)).map((line) =>
    buildTree(line)
  );
}

export function readSnailfishNumber(line: string): Node {
  return buildTree(eval(line));
}

function findClosestLeft(node: Node): Node | undefined {
  const visited = new Set<string>();
  visited.add(node.id);
  let found = false;

  while (node.parent) {
    node = node.parent;
    visited.add(node.id);
    if (node.left && !visited.has(node.left.id)) {
      node = node.left;
      found = true;
      break;
    }
  }

  if (!found) {
    return undefined;
  }

  while (node && node.right) {
    node = node.right;
  }

  return node;
}

function findClosestRight(node: Node): Node | undefined {
  const visited = new Set<string>();
  visited.add(node.id);
  let found = false;

  while (node.parent) {
    node = node.parent;
    visited.add(node.id);
    if (node.right && !visited.has(node.right.id)) {
      node = node.right;
      found = true;
      break;
    }
  }

  if (!found) {
    return undefined;
  }

  while (node && node.left) {
    node = node.left;
  }

  return node;
}

export function explode(root: Node, index = 0): boolean {
  let exploded = false;

  if (index >= 4) {
    if (root.left?.value !== undefined && root.right?.value !== undefined) {
      const closestRight = findClosestRight(root);
      if (closestRight) {
        closestRight.value! += root.right?.value;
      }

      const closestLeft = findClosestLeft(root);
      if (closestLeft) {
        closestLeft.value! += root.left?.value;
      }

      root.left = undefined;
      root.right = undefined;
      root.value = 0;

      exploded = true;
    }
  }

  if (!exploded && root.left) {
    exploded = explode(root.left, index + 1);
  }

  if (!exploded && root.right) {
    exploded = explode(root.right, index + 1);
  }

  return exploded;
}

function createSplit(node: Node) {
  node.left = new Node();
  node.left.value = Math.floor(node.value! / 2);
  node.left.parent = node;

  node.right = new Node();
  node.right.value = Math.ceil(node.value! / 2);
  node.right.parent = node;

  node.value = undefined;
}

export function split(root: Node): boolean {
  let splitted = false;

  if (!splitted && root.value! >= 10) {
    createSplit(root);
    splitted = true;
  }

  if (!splitted && root.left) {
    splitted = split(root.left);
  }

  if (!splitted && root.right) {
    splitted = split(root.right);
  }

  return splitted;
}

export function add(left: Node, right: Node): Node {
  const root = new Node();

  root.left = left;
  root.right = right;
  root.value = undefined;

  left.parent = root;
  right.parent = root;

  return root;
}

export function reduce(root: Node) {
  let exploded, splitted;
  do {
    exploded = splitted = false;

    exploded = explode(root);
    splitted = exploded ? splitted : split(root);
  } while (exploded || splitted);
}
