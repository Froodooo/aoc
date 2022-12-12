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

  @doc """
  Converts a zero-indexed map into a multidimensional list.

  ## Example

      iex> matrix = %{0 => %{0 => "x", 1 => "o", 2 => "x"}}
      ...> Matrix.to_list(matrix)
      [["x", "o", "x"]]
  """
  def to_list(matrix) when is_map(matrix) do
    do_to_list(matrix)
  end

  defp do_to_list(matrix) when is_map(matrix) do
    for {_index, value} <- matrix,
        into: [],
        do: do_to_list(value)
  end

  defp do_to_list(other), do: other

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

  def pathfind(matrix, start, finish, visited \\ [], steps \\ 0)

  def pathfind(_matrix, start, finish, _visited, steps) when start == finish, do: steps |> IO.inspect()

  def pathfind(matrix, start, finish, visited, steps) do
    # IO.inspect({start, finish, visited, steps})
    {y, x} = start

    visited = [start] ++ visited

    next_steps = get_next_steps(matrix, x, y, visited) # |> IO.inspect(label: :next)

    if next_steps == [] do
      nil
    else
      next_steps
      |> Enum.map(fn next_step ->
        pathfind(matrix, next_step, finish, visited, steps + 1)
      end)
      |> Enum.min()
    end
  end

  defp get_next_steps(matrix, sx, sy, visited) do
    Enum.filter([{sy - 1, sx}, {sy + 1, sx}, {sy, sx - 1}, {sy, sx + 1}], fn {y, x} ->
      matrix[y][x] != nil and
      ({y, x} not in visited) and
      ((abs(matrix[y][x] - matrix[sy][sx]) <= 1) or ((matrix[sy][sx] == ?S) or (matrix[y][x] == ?E)))
    end)
  end
end
