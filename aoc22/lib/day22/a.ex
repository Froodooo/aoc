defmodule AoC22.Day22.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input(%{trim: false})
    |> String.split("\n\n")
    |> Enum.map(&String.split(&1, "\n"))
    |> parse()
  end

  defp parse([map, [instructions]]) do
    {parse_map(map), parse_instructions(instructions)}
  end

  defp parse_map(map) do
    Enum.reduce(map, {%{}, 1}, fn row, {coordinates, row_number} ->
      {row
       |> String.graphemes()
       |> Enum.reduce({coordinates, 1}, fn char, {coordinates, col_number} ->
         case char do
           " " -> {coordinates, col_number + 1}
           c -> {Map.put(coordinates, {row_number, col_number}, c), col_number + 1}
         end
       end)
       |> elem(0), row_number + 1}
    end)
    |> elem(0)
  end

  defp parse_instructions(instructions) do
    ~r{(R|L)}
    |> Regex.split(instructions, include_captures: true)
    |> Enum.map(fn
      "R" -> "R"
      "L" -> "L"
      number -> String.to_integer(number)
    end)
  end
end
