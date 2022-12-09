defmodule AoC22.Day9.B do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&String.split/1)
    |> Enum.map(fn [direction, amount] -> [direction, String.to_integer(amount)] end)
    |> Enum.reduce({MapSet.new(), {0, 0}, List.duplicate({0, 0}, 9)}, &move/2)
    |> elem(0)
    |> MapSet.to_list()
    |> length()
  end

  defp move([direction, amount], acc) do
    Enum.reduce(0..(amount - 1), acc, fn _index, {visited, {hx, hy}, tail} ->
      case direction do
        "R" -> move_once({visited, {hx + 1, hy}, tail})
        "L" -> move_once({visited, {hx - 1, hy}, tail})
        "U" -> move_once({visited, {hx, hy + 1}, tail})
        "D" -> move_once({visited, {hx, hy - 1}, tail})
      end
    end)
  end

  defp move_once({visited, {nhx, nhy}, tail}) do
    {_head, new_tail} =
      Enum.reduce(tail, {{nhx, nhy}, []}, fn {tx, ty}, {{hx, hy}, new_tail} ->
        {ntx, nty} = move_tail({hx, hy}, {tx, ty})
        {{ntx, nty}, [{ntx, nty} | new_tail]}
      end)

    new_tail_reversed = Enum.reverse(new_tail)

    {MapSet.put(visited, Enum.at(new_tail_reversed, length(new_tail) - 1)), {nhx, nhy},
     new_tail_reversed}
  end

  defp move_tail({hx, hy}, {tx, ty}) do
    cond do
      hx != tx and hy != ty and hy - ty > 1 and hx - tx >= 1 -> {tx + 1, ty + 1}
      hx != tx and hy != ty and hy - ty > 1 and hx - tx <= -1 -> {tx - 1, ty + 1}
      hx != tx and hy != ty and hy - ty < -1 and hx - tx <= -1 -> {tx - 1, ty - 1}
      hx != tx and hy != ty and hy - ty < -1 and hx - tx >= 1 -> {tx + 1, ty - 1}
      hx != tx and hy != ty and hx - tx > 1 and hy - ty >= 1 -> {tx + 1, ty + 1}
      hx != tx and hy != ty and hx - tx > 1 and hy - ty <= -1 -> {tx + 1, ty - 1}
      hx != tx and hy != ty and hx - tx < -1 and hy - ty <= -1 -> {tx - 1, ty - 1}
      hx != tx and hy != ty and hx - tx < -1 and hy - ty >= 1 -> {tx - 1, ty + 1}
      hy == ty and hx - tx > 1 -> {tx + 1, ty}
      hy == ty and hx - tx < -1 -> {tx - 1, ty}
      hx == tx and hy - ty > 1 -> {tx, ty + 1}
      hx == tx and hy - ty < -1 -> {tx, ty - 1}
      true -> {tx, ty}
    end
  end
end
