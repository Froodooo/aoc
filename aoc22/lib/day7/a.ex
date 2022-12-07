defmodule AoC22.Day7.A do
  alias AoC22.Utils
  alias AoC22.Day7.Disk

  @file_size_threshold 100_000

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&String.split/1)
    |> Disk.traverse()
    |> Map.values()
    |> Enum.filter(&(&1 <= @file_size_threshold))
    |> Enum.sum()
  end
end
