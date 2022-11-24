import { isLowerCase, Path, readGraph } from "./common.ts";

const input = await Deno.readTextFile("./day12/day12.txt");

function findPaths(
  graph: Map<string, Set<string>>,
  paths: Path[],
): Path[] {
  const nextPaths = paths.reduce((newPaths, path) => {
    if (path.lastVisited === "end") newPaths.push(path);

    const nextNodes = graph.get(path.lastVisited);
    if (nextNodes) {
      Array.from(nextNodes).forEach((nextNode) => {
        if (
          !isLowerCase(nextNode) ||
          (isLowerCase(nextNode) && !path.smallCaves.has(nextNode)) ||
          (isLowerCase(nextNode) && path.smallCaves.has(nextNode) &&
            !path.twiceVisited)
        ) {
          const newPath = new Path(
            nextNode,
            new Set<string>(path.smallCaves),
            path.twiceVisited,
          );
          if (isLowerCase(nextNode)) {
            newPath.smallCaves.add(nextNode);
            if (path.smallCaves.has(nextNode)) {
              newPath.twiceVisited = true;
            }
          }
          newPaths.push(newPath);
        }
      });
    }

    return newPaths;
  }, new Array<Path>());

  return nextPaths;
}

export function solve(input: string): number {
  const graph = readGraph(input);

  let foundPathsTotal = 0;
  let foundPaths = [new Path("start", new Set<string>())];

  while (true) {
    foundPaths = findPaths(graph, foundPaths);
    if (foundPaths.length === foundPathsTotal) {
      break;
    }

    foundPathsTotal = foundPaths.length;
  }

  return foundPaths.length;
}

console.log(solve(input));
