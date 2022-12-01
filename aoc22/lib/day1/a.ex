defmodule AoC22.Day1.A do
  alias AoC22.Io

  def solve(input) do
    input
    |> Io.input()
    |> Io.to_list("\n\n")
    |> Enum.map(&split_and_parse/1)
    |> Enum.map(&Enum.sum/1)
    |> Enum.max()
  end

  defp split_and_parse(calories) do
    calories
    |> String.split("\n")
    |> Io.to_number()
  end
end
