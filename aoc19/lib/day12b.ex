defmodule Aoc19.Day12b do
  alias Aoc19.Utils.Common

  def start(input_location) do
    input_location
    |> read()
    |> add_velocity()
    |> start_time()
  end

  defp start_time(moons) do
    steps_x = until_repeat(moons, moons, "x")
    steps_y = until_repeat(moons, moons, "y")
    steps_z = until_repeat(moons, moons, "z")

    lcm(steps_x, steps_y, steps_z)
  end

  def lcm(x, y, z), do: lcm(x, lcm(y, z))
  def lcm(0, 0), do: 0
  def lcm(a, b), do: a * b / gcd(a, b) |> trunc()

  def gcd(a, 0), do: a
  def gcd(0, b), do: b
  def gcd(a, b), do: gcd(b, rem(a, b))

  defp until_repeat(original_moons, moons, position, steps \\ 0) do
    moons = step(moons)

    if repeat?(original_moons, moons, position) do
      steps + 1
    else
      until_repeat(original_moons, moons, position, steps + 1)
    end
  end

  defp repeat?(original_moons, moons, position) do
    original = Enum.map(original_moons, &get_position(&1, position))
    current = Enum.map(moons, &get_position(&1, position))
    original == current
  end

  defp get_position({{x, _, _}, {vx, _, _}}, "x"), do: {x, vx}
  defp get_position({{_, y, _}, {_, vy, _}}, "y"), do: {y, vy}
  defp get_position({{_, _, z}, {_, _, vz}}, "z"), do: {z, vz}

  defp step(moons) do
    Enum.map(moons, &apply_gravity(&1, moons))
  end

  defp apply_gravity({{x, y, z}, {vx, vy, vz}} = current_moon, moons) do
    {vx, vy, vz} =
      moons
      |> List.delete(current_moon)
      |> Enum.reduce({vx, vy, vz}, fn {{x2, y2, z2}, _velocity}, {vx, vy, vz} ->
        vx = vx + calculate_velocity(x, x2)
        vy = vy + calculate_velocity(y, y2)
        vz = vz + calculate_velocity(z, z2)
        {vx, vy, vz}
      end)

    {{x + vx, y + vy, z + vz}, {vx, vy, vz}}
  end

  defp calculate_velocity(p1, p2) when p1 < p2, do: 1
  defp calculate_velocity(p1, p2) when p1 > p2, do: -1
  defp calculate_velocity(_p1, _p2), do: 0

  defp add_velocity(moons) do
    Enum.map(moons, fn moon -> {moon, {0, 0, 0}} end)
  end

  defp read(input_location) do
    input_location
    |> Common.read()
    |> Enum.map(&read_moon/1)
  end

  defp read_moon(moon) do
    moon
    |> String.replace("<", "")
    |> String.replace(">", "")
    |> String.split(",", trim: true)
    |> Enum.map(&read_moon_position/1)
    |> List.to_tuple()
  end

  defp read_moon_position(moon_position) do
    moon_position
    |> String.split("=")
    |> Enum.at(1)
    |> String.to_integer()
  end
end
