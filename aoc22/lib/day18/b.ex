defmodule AoC22.Day18.B do
  alias AoC22.Utils

  def solve(input) do
    cubes =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&parse_cube/1)

    {max_x, max_y, max_z} = max_axes(cubes)
    # all_cubes = init_cube(max_x, max_y, max_z)

    unconnected_sides(cubes, {max_x, max_y, max_z})
  end

  defp unconnected_sides(cubes, max_axes) do
    Enum.reduce(cubes, 0, fn {x, y, z}, acc ->
      count({x + 1, y, z}, cubes, max_axes) +
        count({x - 1, y, z}, cubes, max_axes) +
        count({x, y + 1, z}, cubes, max_axes) +
        count({x, y - 1, z}, cubes, max_axes) +
        count({x, y, z + 1}, cubes, max_axes) +
        count({x, y, z - 1}, cubes, max_axes) +
        acc
    end)
  end

  defp count(cube, cubes, max_axes) do
    case interior?([cube], cubes, [], max_axes, false) do
      true -> 0
      false -> 1
    end
  end

  defp interior?([], _cubes, _seen, _max_axes, seen_outside?), do: !seen_outside?

  defp interior?([{x, y, z} | rest], cubes, seen, {max_x, max_y, max_z}, seen_outside?) do
    cond do
      {x, y, z} in cubes ->
        interior?(rest, cubes, seen, {max_x, max_y, max_z}, seen_outside?)

      {x, y, z} in seen ->
        interior?(rest, cubes, seen, {max_x, max_y, max_z}, seen_outside?)

      length(seen) > 5000 ->
        false

      # x <= 0 or x >= max_x or y <= 0 or y >= max_y or z <= 0 or z >= max_z ->
      #   interior?(rest, cubes, seen, {max_x, max_y, max_z}, true)

      true ->
        (rest ++
           [
             {x - 1, y, z},
             {x + 1, y, z},
             {x, y - 1, z},
             {x, y + 1, z},
             {x, y, z - 1},
             {x, y, z + 1}
           ])
        |> interior?(cubes, [{x, y, z} | seen], {max_x, max_y, max_z}, seen_outside?)
    end
  end

  def max_axes(cubes) do
    Enum.reduce(cubes, {0, 0, 0}, fn {x, y, z}, {max_x, max_y, max_z} ->
      max_x = if x > max_x, do: x, else: max_x
      max_y = if y > max_y, do: y, else: max_y
      max_z = if z > max_z, do: z, else: max_z
      {max_x - 1, max_y - 1, max_z - 1}
    end)
  end

  defp parse_cube(line) do
    line
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
    |> List.to_tuple()
  end
end
