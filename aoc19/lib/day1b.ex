defmodule Aoc19.Day1b do
  @moduledoc false

  alias Aoc19.Utils.Common
  alias Aoc19.Utils.Day1, as: Day1Utils

  def start(input_location) do
    input_location
    |> Common.read_numbers()
    |> Enum.reduce(0, &fuel/2)
    |> trunc()
  end

  def fuel(0, total), do: total

  def fuel(mass, total) do
    fuel =
      mass
      |> Day1Utils.fuel()
      |> Kernel.max(0)

    fuel(fuel, total + fuel)
  end
end
