defmodule Aoc19 do
  @moduledoc """
  Documentation for Aoc19.
  """

  def start({day_module, day}) do
    input_location = "input/#{day}"
    day_module.start(input_location)
  end
end
