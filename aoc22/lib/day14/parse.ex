defmodule AoC22.Day14.Parse do
  def rocks(paths) do
    paths
    |> Enum.map(fn path ->
      path
      |> String.split(" -> ")
      |> path()
    end)
    |> rocks_coordinates()
  end

  defp path(path) do
    Enum.map(path, fn coordinate ->
      coordinate
      |> String.split(",")
      |> Enum.map(&String.to_integer/1)
    end)
  end

  defp rocks_coordinates(paths) do
    Enum.reduce(paths, MapSet.new(), &path_coordinates/2)
  end

  defp path_coordinates(path, rocks) do
    path
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.reduce(MapSet.new(), fn [head, tail], rocks ->
      MapSet.union(rocks, head |> coordinates(tail) |> MapSet.new())
    end)
    |> MapSet.union(rocks)
  end

  defp coordinates([x, sy], [x, fy]), do: Enum.map(sy..fy, fn y -> {x, y} end)
  defp coordinates([sx, y], [fx, y]), do: Enum.map(sx..fx, fn x -> {x, y} end)
end
