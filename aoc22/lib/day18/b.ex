defmodule AoC22.Day18.B do
  alias AoC22.Utils

  def solve(input) do
    cubes =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&parse_cube/1)

    {max_x, max_y, max_z} = max_axes(cubes)
    all_cubes = init_cube(max_x, max_y, max_z)

    _trapped_sides =
      all_cubes
      |> trapped(cubes, {max_x, max_y, max_z})
      |> Enum.count()
      |> Kernel.*(6)

    # unconnected_sides(cubes) - trapped_sides

    :result
  end

  defp trapped(all_cubes, cubes, max_axes) do
    Enum.filter(all_cubes, fn cube -> interior?([cube], cubes, max_axes) end)
  end

  defp interior?([], _cubes, _max_axes), do: true

  # Flood-fill (node):
  # 1. Set Q to the empty queue or stack.
  # 2. Add node to the end of Q.
  # 3. While Q is not empty:
  # 4.   Set n equal to the first element of Q.
  # 5.   Remove first element from Q.
  # 6.   If n is Inside:
  #        Set the n
  #        Add the node to the west of n to the end of Q.
  #        Add the node to the east of n to the end of Q.
  #        Add the node to the north of n to the end of Q.
  #        Add the node to the south of n to the end of Q.
  # 7. Continue looping until Q is exhausted.
  # 8. Return.
  defp interior?([{x, y, z} | rest], cubes, max_axes) do
    cond do
      true ->
        Enum.reduce(
          [
            {x - 1, y, z},
            {x + 1, y, z},
            {x, y - 1, z},
            {x, y + 1, z},
            {x, y, z - 1},
            {x, y, z + 1}
          ],
          rest,
          fn cube, queue -> append(queue, cube, cubes, max_axes) end
        )
    end
  end

  defp append(queue, {x, y, z}, cubes, {max_x, max_y, max_z})
       when x >= 0 and y >= 0 and z >= 0 and x <= max_x and y <= max_y and z <= max_z do
    case {x, y, z} in cubes do
      false -> queue ++ [{x, y, z}]
      true -> queue
    end
  end

  defp append(queue, _cube, _cubes, _max_axes), do: queue

  defp init_cube(max_x, max_y, max_z) do
    Enum.flat_map(0..(max_x - 1), fn x ->
      Enum.flat_map(0..(max_y - 1), fn y ->
        Enum.map(0..(max_z - 1), fn z ->
          {x, y, z}
        end)
      end)
    end)
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
