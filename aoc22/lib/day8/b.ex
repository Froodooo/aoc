defmodule AoC22.Day8.B do
  alias AoC22.Utils
  alias AoC22.Day8.Matrix

  def solve(input) do
    input
    |> Utils.input()
    |> Matrix.to_matrix()
    |> count_visible_trees()
    |> Enum.max()
  end

  defp count_visible_trees(trees) do
    Enum.reduce(1..(Enum.count(trees) - 2), [], fn y, scores ->
      Enum.reduce(1..(Enum.count(trees[0]) - 2), scores, fn x, scores ->
        [visible({x, y}, trees) | scores]
      end)
    end)
  end

  defp visible({x, y}, trees) do
    tree = Matrix.get(trees, {x, y})

    visible_from(:top, {x, y}, trees, tree) *
      visible_from(:bottom, {x, y}, trees, tree) *
      visible_from(:left, {x, y}, trees, tree) *
      visible_from(:right, {x, y}, trees, tree)
  end

  defp count_next_trees([_next_tree], _tree, count) do
    {:halt, count + 1}
  end

  defp count_next_trees([next_tree1, next_tree2], tree, count) do
    if next_tree1 >= tree do
      {:halt, count + 1}
    else
      if next_tree2 > next_tree1 do
        {:cont, count + 1}
      else
        {:cont, count + 1}
      end
    end
  end

  defp chunk_trees([tree_pair]), do: [[tree_pair]]
  defp chunk_trees(tree_pair), do: Enum.chunk_every(tree_pair, 2, 1)

  defp visible_from(:top, {x, y}, trees, tree) do
    (y - 1)..0
    |> Enum.reduce([], &[trees[&1][x] | &2])
    |> visible_in_line(tree)
  end

  defp visible_from(:bottom, {x, y}, trees, tree) do
    (y + 1)..(Enum.count(trees) - 1)
    |> Enum.reduce([], &[trees[&1][x] | &2])
    |> visible_in_line(tree)
  end

  defp visible_from(:left, {x, y}, trees, tree) do
    (x - 1)..0
    |> Enum.reduce([], &[trees[y][&1] | &2])
    |> visible_in_line(tree)
  end

  defp visible_from(:right, {x, y}, trees, tree) do
    (x + 1)..(Enum.count(trees[0]) - 1)
    |> Enum.reduce([], &[trees[y][&1] | &2])
    |> visible_in_line(tree)
  end

  defp visible_in_line(trees, tree) do
    trees
    |> Enum.reverse()
    |> chunk_trees()
    |> Enum.reduce_while(0, fn tree_pair, count ->
      count_next_trees(tree_pair, tree, count)
    end)
  end
end
