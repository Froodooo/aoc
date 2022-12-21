defmodule AoC22.Day21.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Map.new(&parse_monkey/1)
    |> resolve()

    :result
  end

  defp resolve(monkeys) do
    Map.new(monkeys, fn {name, operation} ->
      resolve(monkeys, name, operation)
    end)
  end

  defp resolve(_monkeys, name, operation) when is_number(operation), do: {name, operation}

  defp resolve(monkeys, name, operation) do
    {name,
     operation
     |> Enum.reduce([], fn operand, acc ->
       cond do
         is_number(operand) ->
           [operand | acc]

         operand in ["+", "-", "*", "/"] ->
           [operand | acc]

         is_binary(operand) ->
           [Map.get(monkeys, operand, operand) | acc]
       end
     end)
     |> Enum.reverse()}
  end

  defp parse_monkey(monkey) do
    case String.split(monkey, " ") do
      [name, operand1, operator, operand2] ->
        {String.replace(name, ":", ""), [operand1, operator, operand2]}

      [name, number] ->
        {String.replace(name, ":", ""), String.to_integer(number)}
    end
  end
end
