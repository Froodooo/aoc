defmodule AoC22.Day6.A do
  alias AoC22.Utils

  @chunk_size 4

  def solve(input) do
    input
    |> Utils.input()
    |> String.graphemes()
    |> Enum.chunk_every(@chunk_size, 1)
    |> Enum.with_index()
    |> Enum.find(&unique/1)
    |> elem(1)
    |> Kernel.+(@chunk_size)
  end

  defp unique({characters, _index}) do
    characters |> MapSet.new() |> MapSet.to_list() |> length() == @chunk_size
  end
end
