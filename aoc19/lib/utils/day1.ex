defmodule Aoc19.Utils.Day1 do
  @moduledoc false

  def fuel(mass) do
    mass
    |> Kernel./(3)
    |> :math.floor()
    |> Kernel.-(2)
  end
end
