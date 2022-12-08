defmodule AoC22.Day8.B do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> to_2d_map()
    |> count_visible_trees()
  end

  defp count_visible_trees(trees) do
    Enum.reduce(1..(Enum.count(trees) - 2), [], fn y, scores ->
      Enum.reduce(1..(Enum.count(trees[0]) - 2), scores, fn x, scores ->
        [visible({x, y}, trees) | scores]
      end)
    end)
  end

  defp visible({x, y}, trees) do
    IO.inspect({{y, x}, trees[y][x]})
    visible_from_top({x, y}, trees) *
    visible_from_bottom({x, y}, trees) *
    visible_from_left({x, y}, trees) *
    visible_from_right({x, y}, trees)
    |> IO.inspect()
  end

  defp visible_from_top({x, y}, trees) do
    Enum.reduce_while((y - 1)..0, 0, fn next_y, count ->
      if trees[next_y][x] < trees[next_y + 1][x] do
        {:cont, count + 1}
      else
        {:halt, (if count == 0, do: 1, else: count)}
      end
    end)
    |> IO.inspect(label: :top)
  end

  defp visible_from_bottom({x, y}, trees) do
    Enum.reduce_while((y + 1)..(Enum.count(trees) - 1), 0, fn next_y, count ->
      if trees[next_y][x] < trees[next_y - 1][x] do
        {:cont, count + 1}
      else
        {:halt, (if count == 0, do: 1, else: count)}
      end
    end)
    |> IO.inspect(label: :bottom)
  end

  defp visible_from_left({x, y}, trees) do
    Enum.reduce_while((x - 1)..0, 0, fn next_x, count ->
      if trees[y][next_x] < trees[y][next_x + 1] do
        {:cont, count + 1}
      else
        {:halt, (if count == 0, do: 1, else: count)}
      end
    end)
    |> IO.inspect(label: :left)
  end

  defp visible_from_right({x, y}, trees) do
    Enum.reduce_while((x + 1)..(Enum.count(trees[0]) - 1), 0, fn next_x, count ->
      if trees[y][next_x] < trees[y][next_x - 1] do
        {:cont, count + 1}
      else
        {:halt, (if count == 0, do: 1, else: count)}
      end
    end)
    |> IO.inspect(label: :right)
  end

  defp to_2d_map(input) do
    input
    |> String.split("\n")
    |> Enum.with_index()
    |> to_map()
    |> Enum.map(
      &{elem(&1, 0),
       elem(&1, 1) |> String.graphemes() |> Enum.map(fn x -> String.to_integer(x) end) |> Enum.with_index() |> to_map()}
    )
    |> Map.new()
  end

  defp to_map(input) do
    Map.new(input, &{elem(&1, 1), elem(&1, 0)})
  end
end
