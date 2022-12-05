defmodule AoC22.Day5.A do
  alias AoC22.Utils
  alias AoC22.Day5.Parse

  def solve(input) do
    [raw_stacks, raw_instructions] =
      input
      |> Utils.input(nil)
      |> String.split("\n\n")

    stacks = Parse.parse_stacks(raw_stacks)
    instructions = Parse.parse_instructions(raw_instructions)

    instructions
    |> Enum.reduce(stacks, &move/2)
    |> get_first()
    |> Enum.join("")
  end

  defp move([amount, from, to], stacks) do
    Enum.reduce(1..amount, stacks, fn _, stacks ->
      from_crates = Map.get(stacks, from)
      to_crates = Map.get(stacks, to)
      [from_crate | from_crates_rest] = from_crates
      stacks = Map.put(stacks, to, [from_crate | to_crates])
      Map.put(stacks, from, from_crates_rest)
    end)
  end

  defp get_first(stacks) do
    stacks
    |> Enum.reduce([], fn {_, crates}, acc ->
      [hd(crates) | acc]
    end)
    |> Enum.reverse()
  end
end
