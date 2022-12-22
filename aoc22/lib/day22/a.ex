defmodule AoC22.Day22.A do
  alias AoC22.Utils

  def solve(input) do
    {map, instructions} =
      input
      |> Utils.input(%{trim: false})
      |> String.split("\n\n")
      |> Enum.map(&String.split(&1, "\n", trim: true))
      |> parse()

    map
    |> find_start()
    |> traverse(:right, instructions, map)
    |> password()
  end

  defp password({{row, col}, direction}), do: 1000 * row + 4 * col + facing(direction)

  defp facing(:right), do: 0
  defp facing(:down), do: 1
  defp facing(:left), do: 2
  defp facing(:up), do: 3

  defp traverse(current, direction, [], _map), do: {current, direction}

  defp traverse(current, direction, [instruction | instructions], map) do
    case instruction do
      "R" ->
        traverse(current, turn_right(direction), instructions, map)

      "L" ->
        traverse(current, turn_left(direction), instructions, map)

      steps ->
        current
        |> walk(direction, steps, map)
        |> traverse(direction, instructions, map)
    end
  end

  defp walk({row, col}, _direction, 0, _map), do: {row, col}

  defp walk({row, col}, direction, steps, map) do
    {nrow, ncol} = next({row, col}, direction)

    {nrow, ncol} =
      if is_edge?({nrow, ncol}, map), do: wrap({nrow, ncol}, direction, map), else: {nrow, ncol}

    cond do
      is_wall?({nrow, ncol}, map) ->
        {row, col}

      true ->
        walk({nrow, ncol}, direction, steps - 1, map)
    end
  end

  defp next({row, col}, :right), do: {row, col + 1}
  defp next({row, col}, :left), do: {row, col - 1}
  defp next({row, col}, :up), do: {row - 1, col}
  defp next({row, col}, :down), do: {row + 1, col}

  defp is_edge?({row, col}, map), do: !Map.has_key?(map, {row, col})

  defp is_wall?({row, col}, map), do: Map.get(map, {row, col}) == "#"

  defp wrap({row, _col}, :right, map) do
    map
    |> Enum.filter(fn {{r, _c}, _} -> r == row end)
    |> Enum.sort_by(fn {{_r, c}, _} -> c end, :asc)
    |> Enum.at(0)
    |> elem(0)
  end

  defp wrap({row, _col}, :left, map) do
    map
    |> Enum.filter(fn {{r, _c}, _} -> r == row end)
    |> Enum.sort_by(fn {{_r, c}, _} -> c end, :desc)
    |> Enum.at(0)
    |> elem(0)
  end

  defp wrap({_row, col}, :up, map) do
    map
    |> Enum.filter(fn {{_r, c}, _} -> c == col end)
    |> Enum.sort_by(fn {{r, _c}, _} -> r end, :desc)
    |> Enum.at(0)
    |> elem(0)
  end

  defp wrap({_row, col}, :down, map) do
    map
    |> Enum.filter(fn {{_r, c}, _} -> c == col end)
    |> Enum.sort_by(fn {{r, _c}, _} -> r end, :asc)
    |> Enum.at(0)
    |> elem(0)
  end

  defp turn_right(:up), do: :right
  defp turn_right(:right), do: :down
  defp turn_right(:down), do: :left
  defp turn_right(:left), do: :up

  defp turn_left(:up), do: :left
  defp turn_left(:right), do: :up
  defp turn_left(:down), do: :right
  defp turn_left(:left), do: :down

  defp find_start(map) do
    map
    |> Map.keys()
    |> Enum.filter(fn {row, _col} -> row == 1 end)
    |> Enum.sort_by(fn {_row, col} -> col end, :asc)
    |> Enum.at(0)
  end

  defp parse([map, [instructions]]) do
    {parse_map(map), parse_instructions(instructions)}
  end

  defp parse_map(map) do
    Enum.reduce(map, {%{}, 1}, fn row, {coordinates, row_number} ->
      {row
       |> String.graphemes()
       |> Enum.reduce({coordinates, 1}, fn char, {coordinates, col_number} ->
         case char do
           " " -> {coordinates, col_number + 1}
           c -> {Map.put(coordinates, {row_number, col_number}, c), col_number + 1}
         end
       end)
       |> elem(0), row_number + 1}
    end)
    |> elem(0)
  end

  defp parse_instructions(instructions) do
    ~r{(R|L)}
    |> Regex.split(instructions, include_captures: true)
    |> Enum.map(fn
      "R" -> "R"
      "L" -> "L"
      number -> String.to_integer(number)
    end)
  end
end
