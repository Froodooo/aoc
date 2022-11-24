defmodule Aoc19.Day1a do
  @moduledoc false

  alias Aoc19.Utils.Common
  alias Aoc19.Utils.Day1, as: Day1Utils

  def start(input_location) do
    input_location
    |> Common.read_numbers()
    |> Enum.map(&Day1Utils.fuel/1)
    |> Enum.sum()
    |> trunc()
  end
end
