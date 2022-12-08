defmodule AoC22.Day8.A do
  alias AoC22.Utils
  alias AoC22.Day8.Matrix

  @number_of_corner_trees 4
  @number_of_trees_to_skip 1

  def solve(input) do
    input
    |> Utils.input()
    |> Matrix.to_matrix()
    |> count_visible_trees()
  end

  defp count_visible_trees(trees) do
    1..(Enum.count(trees) - 1 - @number_of_trees_to_skip)
    |> Enum.reduce(0, fn y, count ->
      Enum.reduce(1..(Enum.count(trees[0]) - 2), count, fn x, count ->
        if visible?({x, y}, trees), do: count + 1, else: count
      end)
    end)
    |> Kernel.+(Enum.count(trees) * 2 + Enum.count(trees[0]) * 2 - @number_of_corner_trees)
  end

  defp visible?(tree_position, trees) do
    tree = Matrix.get(trees, tree_position)

    visible_from?(:top, tree_position, trees, tree) or
      visible_from?(:bottom, tree_position, trees, tree) or
      visible_from?(:left, tree_position, trees, tree) or
      visible_from?(:right, tree_position, trees, tree)
  end

  defp visible_from?(:top, {x, y}, trees, tree), do: Enum.all?(0..(y - 1), &(trees[&1][x] < tree))

  defp visible_from?(:bottom, {x, y}, trees, tree),
    do: Enum.all?((Enum.count(trees) - 1)..(y + 1), &(trees[&1][x] < tree))

  defp visible_from?(:left, {x, y}, trees, tree),
    do: Enum.all?(0..(x - 1), &(trees[y][&1] < tree))

  defp visible_from?(:right, {x, y}, trees, tree),
    do: Enum.all?((Enum.count(trees[0]) - 1)..(x + 1), &(trees[y][&1] < tree))
end
