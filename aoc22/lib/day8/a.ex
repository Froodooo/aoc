defmodule AoC22.Day8.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> to_2d_map()
    |> count_visible_trees()
  end

  defp count_visible_trees(trees) do
    Enum.reduce(1..(Enum.count(trees) - 2), 0, fn y, count ->
      Enum.reduce(1..(Enum.count(trees[0]) - 2), count, fn x, count ->
        if visible?({x, y}, trees) do
          count + 1
        else
          count
        end
      end)
    end)
    |> Kernel.+((Enum.count(trees) * 2) + (Enum.count(trees[0]) * 2) - 4)
  end

  defp visible?({x, y}, trees) do
    visible_from_top?({x, y}, trees) or
    visible_from_bottom?({x, y}, trees) or
    visible_from_left?({x, y}, trees) or
    visible_from_right?({x, y}, trees)
  end

  defp visible_from_top?({x, y}, trees) do
    tree = trees[y][x]
    Enum.all?(0..(y - 1), &(trees[&1][x] < tree))
  end

  defp visible_from_bottom?({x, y}, trees) do
    tree = trees[y][x]
    Enum.all?((Enum.count(trees)-1)..(y + 1), &(trees[&1][x] < tree))
  end

  defp visible_from_left?({x, y}, trees) do
    tree = trees[y][x]
    Enum.all?(0..(x - 1), &(trees[y][&1] < tree))
  end

  defp visible_from_right?({x, y}, trees) do
    tree = trees[y][x]
    Enum.all?((Enum.count(trees[0])-1)..(x + 1), &(trees[y][&1] < tree))
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
