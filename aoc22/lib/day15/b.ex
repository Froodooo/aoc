@moduledoc """
  Unfinished
"""
defmodule AoC22.Day15.B do
  alias AoC22.Utils
  alias AoC22.Day15.Sensor

  # Set max to a default of 4000000 for the real input
  def solve(input, max \\ 20) do
    {_min_x, _max_x, sensors} =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.reduce({nil, nil, []}, &parse/2)

    edge_coordinates =
      Enum.reduce(Enum.with_index(sensors), MapSet.new(), fn {sensor, _index}, edge_coordinates ->
        # IO.inspect(index + 1)
        edge_coordinates = elem(edge_coordinates_topright(sensor, edge_coordinates), 1)
        edge_coordinates = elem(edge_coordinates_bottomright(sensor, edge_coordinates), 1)
        edge_coordinates = elem(edge_coordinates_bottomleft(sensor, edge_coordinates), 1)
        edge_coordinates = elem(edge_coordinates_topleft(sensor, edge_coordinates), 1)
        edge_coordinates
      end)

    [{x, y}] =
      edge_coordinates
      |> MapSet.to_list()
      |> Enum.filter(fn {x, y} -> x >= 0 and y >= 0 and x <= max and y <= max end)
      |> Enum.reject(fn {x, y} -> covered_by_sensor?(sensors, x, y) end)
      # |> IO.inspect()

    x * 4_000_000 + y
  end

  defp edge_coordinates_topright(sensor, edge_coordinates) do
    Enum.reduce(
      elem(sensor.position, 0)..(elem(sensor.position, 0) + sensor.manhattan),
      {elem(sensor.position, 1) - sensor.manhattan, edge_coordinates},
      fn x, {y, edge_coordinates} ->
        {y + 1, MapSet.put(edge_coordinates, {x, y - 1})}
      end
    )
  end

  defp edge_coordinates_bottomright(sensor, edge_coordinates) do
    Enum.reduce(
      (elem(sensor.position, 0) + sensor.manhattan)..elem(sensor.position, 0),
      {elem(sensor.position, 1), edge_coordinates},
      fn x, {y, edge_coordinates} ->
        {y + 1, MapSet.put(edge_coordinates, {x + 1, y})}
      end
    )
  end

  defp edge_coordinates_bottomleft(sensor, edge_coordinates) do
    Enum.reduce(
      elem(sensor.position, 0)..(elem(sensor.position, 0) - sensor.manhattan),
      {elem(sensor.position, 1) + sensor.manhattan, edge_coordinates},
      fn x, {y, edge_coordinates} ->
        {y - 1, MapSet.put(edge_coordinates, {x, y + 1})}
      end
    )
  end

  defp edge_coordinates_topleft(sensor, edge_coordinates) do
    Enum.reduce(
      (elem(sensor.position, 0) - sensor.manhattan)..elem(sensor.position, 0),
      {elem(sensor.position, 1), edge_coordinates},
      fn x, {y, edge_coordinates} ->
        {y - 1, MapSet.put(edge_coordinates, {x - 1, y})}
      end
    )
  end

  defp parse(line, {min_x, max_x, sensors}) do
    [_, sensor, beacon] = Regex.run(~r/Sensor at (.*): closest beacon is at (.*)/, line)

    sensor_coordinate = parse_coordinate(sensor)
    beacon_coordinate = parse_coordinate(beacon)

    manhattan = manhattan_distance(sensor_coordinate, beacon_coordinate)

    min_x =
      if min_x == nil,
        do: elem(sensor_coordinate, 0) - manhattan,
        else: Enum.min([min_x, elem(sensor_coordinate, 0) - manhattan])

    max_x =
      if max_x == nil,
        do: elem(sensor_coordinate, 0) + manhattan,
        else: Enum.max([max_x, elem(sensor_coordinate, 0) + manhattan])

    {min_x, max_x,
     [
       %Sensor{
         position: sensor_coordinate,
         closest_beacon: beacon_coordinate,
         manhattan: manhattan
       }
       | sensors
     ]}
  end

  defp parse_coordinate(coordinate_string) do
    [["x", x], ["y", y]] =
      coordinate_string
      |> String.split(", ")
      |> Enum.map(&String.split(&1, "="))

    {String.to_integer(x), String.to_integer(y)}
  end

  defp manhattan_distance({x1, y1}, {x2, y2}) do
    # IO.inspect({x1, y1, x2, y2})
    abs(x1 - x2) + abs(y1 - y2)
  end

  # defp covered_coordinates(sensors, min_x, max_x, y, checked) do
  #   Enum.reduce(min_x..max_x, {[], checked}, fn x, {acc, checked} ->
  #     cond do
  #       MapSet.member?(checked, {x, y}) ->
  #         {acc, checked}

  #       covered_by_sensor?(sensors, x, y) ->
  #         {[{x, y} | acc], MapSet.put(checked, {x, y})}

  #       true ->
  #         {acc, MapSet.put(checked, {x, y})}
  #     end
  #   end)
  # end

  defp covered_by_sensor?(sensors, x, y) do
    Enum.any?(sensors, fn sensor ->
      manhattan_distance(sensor.position, {x, y}) <= sensor.manhattan
    end)
  end

  # defp covered_by_beacon?(sensors, x, y) do
  #   Enum.any?(sensors, fn sensor -> sensor.closest_beacon == {x, y} end)
  # end
end
