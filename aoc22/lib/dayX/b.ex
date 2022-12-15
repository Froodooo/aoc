defmodule AoC22.Day15.B do
  alias AoC22.Utils
  alias AoC22.Day15.Sensor

  def solve(input, max \\ 4000000) do
    {_min_x, max_x, sensors} =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.reduce({nil, nil, []}, &parse/2)

    min = 0
    max = Enum.min([max, max_x])

    y = Enum.find(min..max, fn y ->
      covered = covered_coordinates(sensors, min, max, y)
      Enum.count(covered) < max + 1
    end)

    covered_x = covered_coordinates(sensors, min, max, y) |> Enum.map(&elem(&1, 0))
    x = Enum.to_list(min..max) -- covered_x |> Enum.at(0)
    x * 4000000 + y
  end

  defp parse(line, {min_x, max_x, sensors}) do
    [_, sensor, beacon] = Regex.run(~r/Sensor at (.*): closest beacon is at (.*)/, line)

    sensor_coordinate = parse_coordinate(sensor)
    beacon_coordinate = parse_coordinate(beacon)

    manhattan = manhattan_distance(sensor_coordinate, beacon_coordinate)

    min_x = if min_x == nil, do: elem(sensor_coordinate, 0) - manhattan, else: Enum.min([min_x, elem(sensor_coordinate, 0) - manhattan])
    max_x = if max_x == nil, do: elem(sensor_coordinate, 0) + manhattan, else:  Enum.max([max_x, elem(sensor_coordinate, 0) + manhattan])

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

  defp covered_coordinates(sensors, min_x, max_x, y) do
    Enum.reduce(min_x..max_x, [], fn x, acc ->
      if covered_by_sensor?(sensors, x, y) do
        [{x, y} | acc]
      else
        acc
      end
    end)
  end

  defp covered_by_sensor?(sensors, x, y) do
    Enum.any?(sensors, fn sensor ->
      manhattan_distance(sensor.position, {x, y}) <= sensor.manhattan
    end)
  end

  defp covered_by_beacon?(sensors, x, y) do
    Enum.any?(sensors, fn sensor -> sensor.closest_beacon == {x, y} end)
  end
end
