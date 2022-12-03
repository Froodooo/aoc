defmodule AoC22.Day1.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n\n")
    |> Enum.map(&split_and_parse/1)
    |> Enum.map(&Enum.sum/1)
    |> Enum.max()
  end

  defp split_and_parse(calories) do
    calories
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end
end
