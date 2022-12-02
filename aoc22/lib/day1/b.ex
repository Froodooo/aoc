defmodule AoC22.Day1.B do
  alias AoC22.Io

  def solve(input) do
    input
    |> Io.input()
    |> String.split("\n\n")
    |> Enum.map(&split_and_parse/1)
    |> Enum.map(&Enum.sum/1)
    |> Enum.sort(:desc)
    |> Enum.take(3)
    |> Enum.sum()
  end

  defp split_and_parse(calories) do
    calories
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end
end
