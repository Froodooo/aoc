defmodule AoC22.Day14.B do
  alias AoC22.Utils
  alias AoC22.Day14.Parse

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Parse.rocks()
    |> sandfall(0)
  end

  defp sandfall(rocks, count) do
    lowest = rocks |> MapSet.to_list() |> Enum.map(&elem(&1, 1)) |> Enum.max() |> Kernel.+(2)
    do_sandfall(rocks, lowest, count)
  end

  defp do_sandfall(rocks, lowest, count) do
    case fall(rocks, {500, 0}, lowest) do
      {500, 0} -> count + 1
      {x, y} -> do_sandfall(MapSet.put(rocks, {x, y}), lowest, count + 1)
    end
  end

  defp fall(_rocks, {x, y}, lowest) when y == lowest - 1, do: {x, y}

  defp fall(rocks, {x, y}, lowest) do
    case blocked_below?(rocks, {x, y}) do
      true ->
        cond do
          flow_left?(rocks, {x, y}) -> fall(rocks, {x - 1, y + 1}, lowest)
          flow_right?(rocks, {x, y}) -> fall(rocks, {x + 1, y + 1}, lowest)
          true -> {x, y}
        end

      false ->
        fall(rocks, {x, y + 1}, lowest)
    end
  end

  defp blocked_below?(rocks, {x, y}), do: MapSet.member?(rocks, {x, y + 1})

  defp flow_left?(rocks, {x, y}), do: !MapSet.member?(rocks, {x - 1, y + 1})
  defp flow_right?(rocks, {x, y}), do: !MapSet.member?(rocks, {x + 1, y + 1})
end
