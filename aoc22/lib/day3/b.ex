defmodule AoC22.Day3.B do
  alias AoC22.Utils

  @elf_group_size 3
  @uppercase_offset 26

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&to_mapset/1)
    |> Enum.chunk_every(@elf_group_size)
    |> Enum.map(&find_duplicate/1)
    |> Enum.map(&priority/1)
    |> Enum.sum()
  end

  defp to_mapset(rucksack), do: rucksack |> String.graphemes() |> MapSet.new()

  defp find_duplicate([item]), do: item |> MapSet.to_list() |> Enum.fetch!(0)

  defp find_duplicate([rucksack1, rucksack2 | rest]),
    do: find_duplicate([MapSet.intersection(rucksack1, rucksack2) | rest])

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
