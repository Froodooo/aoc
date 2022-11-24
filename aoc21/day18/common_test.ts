import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";
import { buildTree, explode, split } from "./common.ts";

Deno.test("buildTree", () => {
  const list1 = [[[[[9, 8], 1], 2], 3], 4];
  assertEquals(buildTree(list1).toString(), "[[[[[9,8],1],2],3],4]");

  const list2 = [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]];
  assertEquals(
    buildTree(list2).toString(),
    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
  );
});

Deno.test("explode", () => {
  const node1 = buildTree([[[[[9, 8], 1], 2], 3], 4]);
  explode(node1);
  assertEquals(node1.toString(), "[[[[0,9],2],3],4]");

  const node2 = buildTree([7, [6, [5, [4, [3, 2]]]]]);
  explode(node2);
  assertEquals(node2.toString(), "[7,[6,[5,[7,0]]]]");

  const node3 = buildTree([[6, [5, [4, [3, 2]]]], 1]);
  explode(node3);
  assertEquals(node3.toString(), "[[6,[5,[7,0]]],3]");

  const node4 = buildTree([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]);
  explode(node4);
  assertEquals(node4.toString(), "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]");

  const node5 = buildTree([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]);
  explode(node5);
  assertEquals(node5.toString(), "[[3,[2,[8,0]]],[9,[5,[7,0]]]]");
});

Deno.test("split", () => {
  const node1 = buildTree([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]);
  split(node1);
  assertEquals(node1.toString(), "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]");

  const node2 = buildTree([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]);
  split(node2);
  assertEquals(node2.toString(), "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]");
});
