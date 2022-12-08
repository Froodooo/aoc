defmodule AoC22.Day8.Matrix do
  def to_matrix(input) do
    input
    |> String.split("\n")
    |> Enum.with_index()
    |> to_map()
    |> Map.new(fn {index, treeline} ->
      {
        index,
        treeline
        |> String.graphemes()
        |> Enum.map(&String.to_integer/1)
        |> Enum.with_index()
        |> to_map()
      }
    end)
  end

  def get(matrix, {x, y}) do
    matrix[y][x]
  end

  defp to_map(input), do: Map.new(input, &{elem(&1, 1), elem(&1, 0)})
end
