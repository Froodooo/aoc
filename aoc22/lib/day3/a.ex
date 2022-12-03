defmodule AoC22.Day3.A do
  alias AoC22.Utils

  @rucksack_parts 2
  @uppercase_offset 26

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&find_duplicate/1)
    |> Enum.map(&priority/1)
    |> Enum.sum()
  end

  defp find_duplicate(rucksack) do
    rucksack
    |> divide_in(@rucksack_parts)
    |> intersect()
  end

  defp divide_in(rucksack, parts) do
    rucksack
    |> String.graphemes()
    |> Enum.chunk_every(rucksack |> String.length() |> Kernel./(parts) |> trunc())
    |> Enum.map(&MapSet.new/1)
  end

  defp intersect([compartment1, compartment2]) do
    compartment1
    |> MapSet.intersection(compartment2)
    |> MapSet.to_list()
    |> Enum.fetch!(0)
  end

  defp priority(item) do
    ascii = item |> String.to_charlist() |> hd()

    cond do
      ascii < "a" |> String.to_charlist() |> hd() ->
        @uppercase_offset + ascii - ("A" |> String.to_charlist() |> hd()) + 1

      true ->
        ascii - ("a" |> String.to_charlist() |> hd()) + 1
    end
  end
end
