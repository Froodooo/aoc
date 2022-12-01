defmodule AoC22 do
  @spec solve(non_neg_integer(), non_neg_integer()) :: any
  def solve(day, part) do
    module = String.to_existing_atom("Elixir.AoC22.Day#{day}.#{if part == 1, do: "A", else: "B"}")
    module.solve(day)
  end
end
