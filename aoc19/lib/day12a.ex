defmodule Aoc19.Day12a do
  alias Aoc19.Utils.Common

  @default_steps 1000

  def start(input_location, steps \\ @default_steps) do
    input_location
    |> read()
    |> add_velocity()
    |> start_time(steps)
    |> energy()
  end

  defp energy(moons) do
    Enum.reduce(moons, 0, fn moon, total_energy ->
      total_energy + potential_energy(moon) * kinetic_energy(moon)
    end)
  end

  defp potential_energy({{x, y, z}, _velocity}) do
    abs(x) + abs(y) + abs(z)
  end

  defp kinetic_energy({_position, {vx, vy, vz}}) do
    abs(vx) + abs(vy) + abs(vz)
  end

  defp start_time(moons, steps) when steps > 0 do
    moons
    |> step()
    |> start_time(steps - 1)
  end

  defp start_time(moons, _steps), do: moons

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
