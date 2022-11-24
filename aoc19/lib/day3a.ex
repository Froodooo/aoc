defmodule Aoc19.Day3a do
  @moduledoc false

  alias Aoc19.Utils.Common

  def start(input_location) do
    [line1, line2] =
      input_location
      |> read()
      |> paths()

    line1
    |> MapSet.intersection(line2)
    |> Enum.map(&distance/1)
    |> Enum.min()
  end

  defp distance({x, y}) do
    abs(x) + abs(y)
  end

  defp paths(instructions) do
    instructions
    |> Enum.map(&path/1)
  end

  defp path(instructions) do
    {_, full_path} =
      Enum.reduce(instructions, {{0, 0}, []}, fn instruction,
                                                 {coordinate, path} ->
        walk(coordinate, path, instruction)
      end)

    MapSet.new(full_path)
  end

  defp walk({x, y}, path, {"R", steps}) do
    coordinates =
      for n <- 1..steps do
        {x + n, y}
      end

    {{x + steps, y}, Enum.concat(path, coordinates)}
  end

  defp walk({x, y}, path, {"L", steps}) do
    coordinates =
      for n <- 1..steps do
        {x - n, y}
      end

    {{x - steps, y}, Enum.concat(path, coordinates)}
  end

  defp walk({x, y}, path, {"U", steps}) do
    coordinates =
      for n <- 1..steps do
        {x, y + n}
      end

    {{x, y + steps}, Enum.concat(path, coordinates)}
  end

  defp walk({x, y}, path, {"D", steps}) do
    coordinates =
      for n <- 1..steps do
        {x, y - n}
      end

    {{x, y - steps}, Enum.concat(path, coordinates)}
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
