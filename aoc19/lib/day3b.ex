defmodule Aoc19.Day3b do
  @moduledoc false

  alias Aoc19.Utils.Common

  def start(input_location) do
    [line1, line2] =
      input_location
      |> read()
      |> paths()

    line1_coordinates = coordinates(line1)
    line2_coordinates = coordinates(line2)

    line1_coordinates
    |> MapSet.intersection(line2_coordinates)
    |> Enum.map(&distance(&1, line1, line2))
    |> Enum.min()
  end

  defp coordinates(line) do
    line
    |> Enum.map(&remove_distance/1)
    |> MapSet.new()
  end

  defp remove_distance({x, y, _d}), do: {x, y}

  defp distance({x, y}, line1, line2) do
    {_, _, d1} = Enum.find(line1, fn {x1, y1, _} -> x == x1 && y == y1 end)
    {_, _, d2} = Enum.find(line2, fn {x2, y2, _} -> x == x2 && y == y2 end)
    d1 + d2
  end

  defp paths(instructions) do
    instructions
    |> Enum.map(&path/1)
  end

  defp path(instructions) do
    {_, full_path} =
      Enum.reduce(instructions, {{0, 0, 0}, []}, fn instruction,
                                                    {coordinate, path} ->
        walk(coordinate, path, instruction)
      end)

    full_path
  end

  defp walk({x, y, d}, path, {"R", steps}) do
    coordinates =
      for n <- 1..steps do
        {x + n, y, d + n}
      end

    {{x + steps, y, d + steps}, Enum.concat(path, coordinates)}
  end

  defp walk({x, y, d}, path, {"L", steps}) do
    coordinates =
      for n <- 1..steps do
        {x - n, y, d + n}
      end

    {{x - steps, y, d + steps}, Enum.concat(path, coordinates)}
  end

  defp walk({x, y, d}, path, {"U", steps}) do
    coordinates =
      for n <- 1..steps do
        {x, y + n, d + n}
      end

    {{x, y + steps, d + steps}, Enum.concat(path, coordinates)}
  end

  defp walk({x, y, d}, path, {"D", steps}) do
    coordinates =
      for n <- 1..steps do
        {x, y - n, d + n}
      end

    {{x, y - steps, d + steps}, Enum.concat(path, coordinates)}
  end

  defp walk(_, _, _), do: {nil, nil}

  defp read(input_location) do
    input_location
    |> Common.read_lines()
    |> Enum.map(&String.split(&1, ","))
    |> Enum.map(&instructions/1)
  end

  defp instructions(line) do
    Enum.map(line, &instruction/1)
  end

  defp instruction(<<direction::binary-size(1)>> <> number) do
    {direction, String.to_integer(number)}
  end
end
