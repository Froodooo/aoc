defmodule AoC22.Day1.B do
  alias AoC22.Io

  def solve(year, day, input \\ nil) do
    year
    |> Io.input(day, input)
    |> Io.to_list("\n\n")
    |> Enum.map(&split_and_parse/1)
    |> Enum.map(&Enum.sum/1)
    |> Enum.sort(:desc)
    |> Enum.take(3)
    |> Enum.sum()
  end

  defp split_and_parse(calories) do
    calories
    |> String.split("\n")
    |> Io.to_number()
  end
end
