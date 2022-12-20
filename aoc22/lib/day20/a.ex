defmodule AoC22.Day20.A do
  alias AoC22.Utils

  def solve(input) do
    indexed_list =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&String.to_integer/1)
      |> Enum.with_index()

    list_length = length(indexed_list)

    resulting_list =
      indexed_list
      |> Enum.reduce(indexed_list, fn indexed_value, acc ->
        move(indexed_value, acc, list_length)
      end)
      |> Enum.map(fn {value, _index} -> value end)

    index_0 = Enum.find_index(resulting_list, fn value -> value == 0 end)

    Enum.at(resulting_list, rem(1000 + index_0, list_length)) +
      Enum.at(resulting_list, rem(2000 + index_0, list_length)) +
      Enum.at(resulting_list, rem(3000 + index_0, list_length))
  end

  defp move({value, initial_index}, acc, list_length) do
    current_index = Enum.find_index(acc, fn {_, index} -> index == initial_index end)
    new_index = rem(current_index + value, list_length - 1)

    {l, r} = acc |> List.delete_at(current_index) |> Enum.split(new_index)
    l ++ [{value, initial_index}] ++ r
  end
end
