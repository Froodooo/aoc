defmodule AoC22.Day18.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&parse_cube/1)
    |> unconnected_sides()
  end

  defp unconnected_sides(cubes) do
    Enum.reduce(cubes, 0, fn {x, y, z}, acc ->
      count({x + 1, y, z}, cubes) +
        count({x - 1, y, z}, cubes) +
        count({x, y + 1, z}, cubes) +
        count({x, y - 1, z}, cubes) +
        count({x, y, z + 1}, cubes) +
        count({x, y, z - 1}, cubes) +
        acc
    end)
  end

  defp count(cube, cubes) do
    case Enum.any?(cubes, &(&1 == cube)) do
      true -> 0
      false -> 1
    end
  end

  defp parse_cube(line) do
    line
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
    |> List.to_tuple()
  end
end
