const day = Deno.args[0];

// Directory
Deno.mkdir(`./day${day}`);

// Code part A and B
const dayContents =
  `const input = await Deno.readTextFile("./day${day}/day${day}.txt");

console.log(input);`;

await Deno.writeTextFile(`./day${day}/day${day}a.ts`, dayContents);
await Deno.writeTextFile(`./day${day}/day${day}b.ts`, dayContents);

// Test part A and B
const dayTestContents =
  `import { assertEquals } from "https://deno.land/std@0.116.0/testing/asserts.ts";

Deno.test("Example 1", async () => {
  const input = await Deno.readTextFile("./day${day}/day${day}_ex.txt");
  assertEquals(true, true);
});`;

await Deno.writeTextFile(`./day${day}/day${day}a_test.ts`, dayTestContents);
await Deno.writeTextFile(`./day${day}/day${day}b_test.ts`, dayTestContents);

// Input files
await Deno.writeTextFile(`./day${day}/day${day}.txt`, "");
await Deno.writeTextFile(`./day${day}/day${day}_ex.txt`, "");
