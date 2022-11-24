defmodule Aoc19.Day6a do
  @moduledoc false

  alias Aoc19.Utils.Common

  def start(input_location) do
    input_location
    |> read()
    |> orbits()
  end

  defp orbits(orbit_map) do
    Enum.reduce(orbit_map, 0, &count(&1, &2, orbit_map)) +
      length(Map.keys(orbit_map))
  end

  defp count({_orbits, orbited}, total_orbits, orbit_map) do
    next_orbit? = Map.has_key?(orbit_map, orbited)
    continue(next_orbit?, orbited, total_orbits, orbit_map)
  end

  defp continue(true, orbits, total_orbits, orbit_map) do
    orbited = Map.fetch!(orbit_map, orbits)
    count({orbits, orbited}, total_orbits + 1, orbit_map)
  end

  defp continue(false, _, total_orbits, _orbit_map), do: total_orbits

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
