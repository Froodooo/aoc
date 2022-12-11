defmodule AoC22.Day11.B do
  alias AoC22.Utils
  alias AoC22.Day11.Monkey

  def solve(input) do
    monkeys =
      input
      |> Utils.input()
      |> String.split("\n\n")
      |> Enum.map(&Monkey.parse/1)
      |> to_map()

    test_product =
      monkeys
      |> Enum.reduce([], fn {_, %Monkey{test: test}}, acc ->
        [test | acc]
      end)
      |> Enum.product()

    monkeys
    |> run(test_product)
    |> most_active()
    |> Enum.product()
  end

  defp most_active(monkeys) do
    monkeys
    |> Enum.reduce([], fn {_, %Monkey{inspected: inspected}}, acc ->
      [inspected | acc]
    end)
    |> Enum.sort(:desc)
    |> Enum.take(2)
  end

  defp to_map(monkeys) do
    monkeys
    |> Enum.with_index()
    |> Enum.map(fn {k, v} -> {v, k} end)
    |> Map.new()
  end

  defp run(monkeys, test_product) do
    Enum.reduce(1..10000, monkeys, fn _, acc ->
      do_round(acc, test_product)
    end)
  end

  defp do_round(monkeys, test_product) do
    Enum.reduce(0..(Enum.count(monkeys) - 1), monkeys, &update_in_round(&1, &2, test_product))
  end

  defp update_in_round(index, monkeys, test_product) do
    monkeys =
      update_in(monkeys, [Access.key!(index)], fn monkey ->
        %Monkey{monkey | inspected: monkey.inspected + length(monkey.items)}
      end)

    do_turn(monkeys[index], monkeys, test_product)
  end

  defp do_turn(%Monkey{items: items} = monkey, monkeys, test_product) do
    Enum.reduce(items, monkeys, &update_in_turn(&1, &2, monkey, test_product))
  end

  defp update_in_turn(
         item,
         monkeys,
         %Monkey{
           monkey: nr,
           operation: operation,
           test: test,
           test_true: test_true,
           test_false: test_false
         },
         test_product
       ) do
    new_item =
      item
      |> do_operation(operation)
      |> rem(test_product)

    # |> do_bored()

    throw_to =
      new_item
      |> throw_to(test, test_true, test_false)

    monkeys =
      update_in(monkeys, [Access.key!(throw_to), Access.key!(:items)], fn current_items ->
        current_items ++ [new_item]
      end)

    monkeys =
      update_in(monkeys, [Access.key!(nr), Access.key!(:items)], fn current_items ->
        current_items -- [item]
      end)

    monkeys
  end

  defp do_operation(item, {"*", "old"}), do: item * item
  defp do_operation(item, {"+", "old"}), do: item + item
  defp do_operation(item, {"*", term}), do: item * term
  defp do_operation(item, {"+", term}), do: item + term

  defp throw_to(item, test, test_true, test_false) do
    if rem(item, test) == 0, do: test_true, else: test_false
  end
end
