defmodule AoC22.Day11.A do
  alias AoC22.Utils
  alias AoC22.Day11.{Monkey, Operation}

  @rounds 20
  @bored_divider 3

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n\n")
    |> Enum.map(&Monkey.parse/1)
    |> Monkey.to_map()
    |> run()
    |> Monkey.most_active()
    |> Enum.product()
  end

  defp run(monkeys) do
    Enum.reduce(1..@rounds, monkeys, fn _, acc ->
      do_round(acc)
    end)
  end

  defp do_round(monkeys) do
    Enum.reduce(0..(Enum.count(monkeys) - 1), monkeys, &update_in_round/2)
  end

  defp update_in_round(index, monkeys) do
    monkeys =
      update_in(monkeys, [Access.key!(index)], fn monkey ->
        %Monkey{monkey | inspected: monkey.inspected + length(monkey.items)}
      end)

    do_turn(monkeys[index], monkeys)
  end

  defp do_turn(%Monkey{items: items} = monkey, monkeys) do
    Enum.reduce(items, monkeys, &update_in_turn(&1, &2, monkey))
  end

  defp update_in_turn(item, monkeys, %Monkey{
         monkey: nr,
         operation: operation,
         test: test,
         test_true: test_true,
         test_false: test_false
       }) do
    new_item =
      item
      |> Operation.execute(operation)
      |> do_bored()

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

  defp do_bored(item), do: trunc(item / @bored_divider)
end
