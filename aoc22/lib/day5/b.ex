defmodule AoC22.Day5.B do
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
    from_crates = Map.get(stacks, from)
    to_crates = Map.get(stacks, to)

    crates_to_move = Enum.take(from_crates, amount)
    from_crates = Enum.drop(from_crates, amount)
    stacks = Map.put(stacks, to, crates_to_move ++ to_crates)
    Map.put(stacks, from, from_crates)
  end

  defp get_first(stacks) do
    stacks
    |> Enum.reduce([], fn {_, crates}, acc ->
      [hd(crates) | acc]
    end)
    |> Enum.reverse()
  end
end
