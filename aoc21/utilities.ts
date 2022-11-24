import { cookie } from "./deps.ts";

export async function fetchInputData(
  year: number,
  day: number,
): Promise<string> {
  const response = await fetch(
    `https://adventofcode.com/${year}/day/${day}/input`,
    {
      headers: {
        cookie: cookie,
      },
    },
  );

  return await response.text();
}

export async function writeInputData(
  day: number,
  inputData: string,
): Promise<void> {
  await Deno.writeTextFile(`./day${day}.txt`, inputData);
}
