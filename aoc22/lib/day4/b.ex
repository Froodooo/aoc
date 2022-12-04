defmodule AoC22.Day4.B do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&parse_pairs/1)
    |> Enum.reduce(0, &intersection/2)
  end

  defp parse_pairs(pairs) do
    pairs
    |> String.split(",")
    |> Enum.map(&parse_sections/1)
  end

  defp parse_sections(sections) do
    sections
    |> String.split("-")
    |> Enum.map(&(&1 |> String.to_integer() |> trunc()))
    |> format_sections()
  end

  defp format_sections([section_start, section_end]), do: Enum.to_list(section_start..section_end)

  defp intersection([], total), do: total

  defp intersection([section1, section2], total) do
    set1 = MapSet.new(section1)
    set2 = MapSet.new(section2)

    cond do
      intersection?(set1, set2) -> total + 1
      intersection?(set2, set1) -> total + 1
      true -> total
    end
  end

  defp intersection?(set1, set2) do
    set1 |> MapSet.intersection(set2) |> MapSet.to_list() |> length() > 0
  end
end
