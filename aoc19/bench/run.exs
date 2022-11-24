days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

inputs =
  days
  |> Enum.reduce(%{}, fn day, map ->
    module_a = String.to_atom("Elixir.Aoc19.Day#{day}a")
    module_b = String.to_atom("Elixir.Aoc19.Day#{day}b")
    map = Map.put(map, "#{day}a", {module_a, Integer.to_string(day)})
    Map.put(map, "#{day}b", {module_b, Integer.to_string(day)})
  end)

Benchee.run(
  %{
    "Days" => fn input -> Aoc19.start(input) end
  },
  warmup: 0,
  inputs: inputs
)
