defmodule AoC22.Day12.Matrix do
  @moduledoc """
  Helpers for working with multidimensional lists, also called matrices.
  """

  @doc """
  Converts a multidimensional list into a zero-indexed map.

  ## Example

      iex> list = [["x", "o", "x"]]
      ...> Matrix.from_list(list)
      %{0 => %{0 => "x", 1 => "o", 2 => "x"}}
  """
  def from_list(list) when is_list(list) do
    do_from_list(list)
  end

  defp do_from_list(list, map \\ %{}, index \\ 0)
  defp do_from_list([], map, _index), do: map

  defp do_from_list([h | t], map, index) do
    map = Map.put(map, index, do_from_list(h))
    do_from_list(t, map, index + 1)
  end

  defp do_from_list(other, _, _), do: other

  def find(matrix, value) do
    {row, _} =
      Enum.find(matrix, fn {_, row} ->
        Enum.find(row, fn {_, cell} ->
          cell == value
        end)
      end)

    {column, _} =
      Enum.find(matrix[row], fn {_, cell} ->
        cell == value
      end)

    {row, column}
  end

  def find_all(matrix, value) do
    for y <- 0..(Enum.count(matrix) - 1),
        x <- 0..(Enum.count(matrix[y]) - 1),
        matrix[y][x] == value,
        do: {{y, x}, 0}
  end

  def bfs(_matrix, [{{y, x}, steps} | _queue], {y, x}, _visited), do: steps

  def bfs(matrix, [{{sy, sx}, steps} | queue], finish, visited) do
    cond do
      {sy, sx} in visited -> bfs(matrix, queue, finish, visited)
      true -> do_bfs(matrix, [{{sy, sx}, steps} | queue], finish, visited)
    end
  end

  defp do_bfs(matrix, [{{sy, sx}, steps} | queue], finish, visited) do
    visited = [{sy, sx} | visited]

    queue =
      Enum.concat(
        queue,
        Enum.filter(
          [
            {{sy - 1, sx}, steps + 1},
            {{sy + 1, sx}, steps + 1},
            {{sy, sx - 1}, steps + 1},
            {{sy, sx + 1}, steps + 1}
          ],
          fn
            {{y, x}, _} ->
              matrix[y][x] != nil and
                {y, x} not in visited and
                matrix[y][x] <= matrix[sy][sx] + 1
          end
        )
      )

    bfs(matrix, queue, finish, visited)
  end
end
