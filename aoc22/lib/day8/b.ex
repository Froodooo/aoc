defmodule AoC22.Day8.B do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> to_2d_map()
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
    visible_from_top({x, y}, trees) *
      visible_from_bottom({x, y}, trees) *
      visible_from_left({x, y}, trees) *
      visible_from_right({x, y}, trees)
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

  defp visible_from_top({x, y}, trees) do
    tree = trees[y][x]

    (y - 1)..0
    |> Enum.reduce([], &[trees[&1][x] | &2])
    |> Enum.reverse()
    |> chunk_trees()
    |> Enum.reduce_while(0, fn tree_pair, count ->
      count_next_trees(tree_pair, tree, count)
    end)
  end

  defp visible_from_bottom({x, y}, trees) do
    tree = trees[y][x]

    (y + 1)..(Enum.count(trees) - 1)
    |> Enum.reduce([], &[trees[&1][x] | &2])
    |> Enum.reverse()
    |> chunk_trees()
    |> Enum.reduce_while(0, fn tree_pair, count ->
      count_next_trees(tree_pair, tree, count)
    end)
  end

  defp visible_from_left({x, y}, trees) do
    tree = trees[y][x]

    (x - 1)..0
    |> Enum.reduce([], &[trees[y][&1] | &2])
    |> Enum.reverse()
    |> chunk_trees()
    |> Enum.reduce_while(0, fn tree_pair, count ->
      count_next_trees(tree_pair, tree, count)
    end)
  end

  defp visible_from_right({x, y}, trees) do
    tree = trees[y][x]

    (x + 1)..(Enum.count(trees[0]) - 1)
    |> Enum.reduce([], &[trees[y][&1] | &2])
    |> Enum.reverse()
    |> chunk_trees()
    |> Enum.reduce_while(0, fn tree_pair, count ->
      count_next_trees(tree_pair, tree, count)
    end)
  end

  defp to_2d_map(input) do
    input
    |> String.split("\n")
    |> Enum.with_index()
    |> to_map()
    |> Enum.map(
      &{elem(&1, 0),
       elem(&1, 1)
       |> String.graphemes()
       |> Enum.map(fn x -> String.to_integer(x) end)
       |> Enum.with_index()
       |> to_map()}
    )
    |> Map.new()
  end

  defp to_map(input) do
    Map.new(input, &{elem(&1, 1), elem(&1, 0)})
  end
end
