defmodule AoC22.Day9.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&String.split/1)
    |> Enum.map(fn [direction, amount] -> [direction, String.to_integer(amount)] end)
    |> Enum.reduce({MapSet.new(), {0, 0}, {0, 0}}, &move/2)
    |> elem(0)
    |> MapSet.to_list()
    |> length()
  end

  defp move([direction, amount], acc) do
    Enum.reduce(0..(amount - 1), acc, &(move_once(direction, &2, &1)))
  end

  defp move_once("R", {visited, {hx, hy}, {tx, ty}}, _index) do
    {ntx, nty} = move_tail({hx + 1, hy}, {tx, ty})
    {MapSet.put(visited, {ntx, nty}), {hx + 1, hy}, {ntx, nty}}
  end

  defp move_once("L", {visited, {hx, hy}, {tx, ty}}, _index) do
    {ntx, nty} = move_tail({hx - 1, hy}, {tx, ty})
    {MapSet.put(visited, {ntx, nty}), {hx - 1, hy}, {ntx, nty}}
  end

  defp move_once("U", {visited, {hx, hy}, {tx, ty}}, _index) do
    {ntx, nty} = move_tail({hx, hy + 1}, {tx, ty})
    {MapSet.put(visited, {ntx, nty}), {hx, hy + 1}, {ntx, nty}}
  end

  defp move_once("D", {visited, {hx, hy}, {tx, ty}}, _index) do
    {ntx, nty} = move_tail({hx, hy - 1}, {tx, ty})
    {MapSet.put(visited, {ntx, nty}), {hx, hy - 1}, {ntx, nty}}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hy - ty > 1 and hx - tx == 1 do
    {tx + 1, ty + 1}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hy - ty > 1 and hx - tx == -1 do
    {tx - 1, ty + 1}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hy - ty < -1 and hx - tx == -1 do
    {tx - 1, ty - 1}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hy - ty < -1 and hx - tx == 1 do
    {tx + 1, ty - 1}
  end


  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hx - tx > 1 and hy - ty == 1 do
    {tx + 1, ty + 1}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hx - tx > 1 and hy - ty == -1 do
    {tx + 1, ty - 1}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hx - tx < -1 and hy - ty == -1 do
    {tx - 1, ty - 1}
  end

  defp move_tail({hx, hy}, {tx, ty}) when hx != tx and hy != ty and hx - tx < -1 and hy - ty == 1 do
    {tx - 1, ty + 1}
  end


  defp move_tail({hx, y}, {tx, y}) when hx - tx > 1 do
    {tx + 1, y}
  end

  defp move_tail({hx, y}, {tx, y}) when hx - tx < -1 do
    {tx - 1, y}
  end

  defp move_tail({x, hy}, {x, ty}) when hy - ty > 1 do
    {x, ty + 1}
  end

  defp move_tail({x, hy}, {x, ty}) when hy - ty < -1 do
    {x, ty - 1}
  end


  defp move_tail(_head, tail), do: tail
end
