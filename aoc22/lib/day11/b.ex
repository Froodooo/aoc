defmodule AoC22.Day11.B do
  alias AoC22.Utils
  alias AoC22.Day11.{Monkey, Operation}

  @rounds 10000

  def solve(input) do
    monkeys =
      input
      |> Utils.input()
      |> String.split("\n\n")
      |> Enum.map(&Monkey.parse/1)
      |> Monkey.to_map()

    test_product = Enum.reduce(monkeys, 1, fn {_, %Monkey{test: test}}, acc -> test * acc end)

    monkeys
    |> run(test_product)
    |> Monkey.most_active()
    |> Enum.product()
  end

  defp run(monkeys, test_product) do
    Enum.reduce(1..@rounds, monkeys, fn _, acc ->
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
      |> Operation.execute(operation)
      |> rem(test_product)

    monkeys
    |> update_in(
      [Access.key!(Monkey.throw_to(new_item, test, test_true, test_false)), Access.key!(:items)],
      fn current_items -> current_items ++ [new_item] end
    )
    |> update_in(
      [Access.key!(nr), Access.key!(:items)],
      fn current_items -> current_items -- [item] end
    )
  end
end
