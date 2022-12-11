defmodule AoC22.Day11.Monkey do
  defstruct monkey: nil,
            items: [],
            operation: nil,
            test: nil,
            test_true: nil,
            test_false: nil,
            inspected: 0

  def parse(input) do
    lines = input |> String.split("\n") |> Enum.map(&String.trim/1)

    %__MODULE__{
      monkey: parse_monkey_number(Enum.at(lines, 0)),
      items: parse_starting(Enum.at(lines, 1)),
      operation: parse_operation(Enum.at(lines, 2)),
      test: parse_test(Enum.at(lines, 3)),
      test_true: parse_test_true(Enum.at(lines, 4)),
      test_false: parse_test_false(Enum.at(lines, 5))
    }
  end

  defp parse_monkey_number(input) do
    input |> String.split(" ") |> List.last() |> String.slice(0..-2) |> String.to_integer()
  end

  defp parse_starting(input) do
    input
    |> String.replace("Starting items: ", "")
    |> String.split(", ")
    |> Enum.map(&String.to_integer/1)
  end

  defp parse_operation(input) do
    [operation, term] = input |> String.replace("Operation: new = old ", "") |> String.split(" ")
    {operation, if(term == "old", do: term, else: String.to_integer(term))}
  end

  defp parse_test(input) do
    input |> String.replace("Test: divisible by ", "") |> String.to_integer()
  end

  defp parse_test_true(input) do
    input |> String.replace("If true: throw to monkey ", "") |> String.to_integer()
  end

  defp parse_test_false(input) do
    input |> String.replace("If false: throw to monkey ", "") |> String.to_integer()
  end

  def most_active(monkeys) do
    monkeys
    |> Enum.reduce([], fn {_, %__MODULE__{inspected: inspected}}, acc ->
      [inspected | acc]
    end)
    |> Enum.sort(:desc)
    |> Enum.take(2)
  end

  def to_map(monkeys) do
    monkeys
    |> Enum.with_index()
    |> Enum.map(fn {k, v} -> {v, k} end)
    |> Map.new()
  end

  def throw_to(item, test, test_true, test_false) do
    if rem(item, test) == 0, do: test_true, else: test_false
  end
end
