# No idea...
defmodule AoC22.Day16.A do
  alias AoC22.Utils
  alias AoC22.Day16.Valve

  def solve(input) do
    valves =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&parse/1)

    starting_valve = Enum.find(valves, &(&1.name == "AA"))

    escape(valves, MapSet.new(), starting_valve, starting_valve.rate, 30)

    :result
  end

  defp parse(line) do
    [_, name, rate, tunnels] =
      Regex.run(~r/Valve (.+) has flow rate=(\d+); tunnels* leads* to valves* (.*)/, line)

    %Valve{name: name, rate: String.to_integer(rate), tunnels: String.split(tunnels, ", ")}
  end

  defp escape(_valves, _visited_valves, _current_valve, rate, minutes) when minutes <= 0,
    do: rate |> IO.inspect()

  defp escape(valves, visited_valves, %Valve{tunnels: _tunnels}, rate, _minutes_left) do
    # IO.inspect({visited_valves, current_valve, rate, minutes_left})

    rate + rate_addition(visited_valves, valves)
  end

  defp rate_addition(visited_valves, valves) do
    visited_valves
    |> MapSet.to_list()
    |> Enum.reduce(0, fn visited_valve, acc ->
      valve = Enum.find(valves, &(&1.name == visited_valve))
      acc + valve.rate
    end)
  end
end
