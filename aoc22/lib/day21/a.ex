defmodule AoC22.Day21.A do
  alias AoC22.Utils

  def solve(input) do
    operations =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Map.new(&parse_monkey/1)

    operations
    |> Map.fetch!("root")
    |> resolve(operations)
  end

  defp resolve([operand1, operator, operand2], operations) do
    case operator do
      "+" -> (resolve(operand1, operations) + resolve(operand2, operations))
      "*" -> (resolve(operand1, operations) * resolve(operand2, operations))
      "/" -> (resolve(operand1, operations) / resolve(operand2, operations))
      "-" -> (resolve(operand1, operations) - resolve(operand2, operations))
    end
    |> trunc()
  end

  defp resolve(operand, _operations) when is_integer(operand), do: operand

  defp resolve(operand, operations) when is_binary(operand) do
    case Map.fetch!(operations, operand) do
      [operand1, operator, operand2] -> resolve([operand1, operator, operand2], operations)
      number -> number
    end
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
