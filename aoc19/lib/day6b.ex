defmodule Aoc19.Day6b do
  @moduledoc false

  alias Aoc19.Utils.Common

  def start(input_location) do
    input_location
    |> read()
    |> paths()
    |> transfers("YOU", "SAN")
  end

  defp transfers(paths, object1, object2) do
    path1 = Map.fetch!(paths, object1)
    path2 = Map.fetch!(paths, object2)
    set1 = MapSet.new(path1)
    set2 = MapSet.new(path2)
    intersection = MapSet.intersection(set1, set2)

    intersection
    |> Enum.map(&distances(&1, [path1, path2]))
    |> Enum.min()
  end

  defp distances(object, paths) do
    paths
    |> Enum.map(fn path ->
      path_distance(path, object, 0)
    end)
    |> Enum.sum()
  end

  defp path_distance([hd | _rest], object, length) when hd == object, do: length

  defp path_distance([_hd | rest], object, length) do
    path_distance(rest, object, length + 1)
  end

  defp paths(orbit_map) do
    Map.new(orbit_map, fn {orbits, orbited} ->
      {orbits,
       orbited
       |> walk([], orbit_map)
       |> Enum.reverse()}
    end)
  end

  defp walk(orbited, path, orbit_map) do
    next_orbit? = Map.has_key?(orbit_map, orbited)
    continue(next_orbit?, orbited, path, orbit_map)
  end

  defp continue(true, orbits, path, orbit_map) do
    orbited = Map.fetch!(orbit_map, orbits)
    walk(orbited, [orbits | path], orbit_map)
  end

  defp continue(false, orbited, path, _orbit_map), do: [orbited | path]

  defp read(input_location) do
    input_location
    |> Common.read_lines()
    |> to_map()
  end

  defp to_map(input) do
    Map.new(input, fn line ->
      [orbited, orbits] = String.split(line, ")")
      {orbits, orbited}
    end)
  end
end
