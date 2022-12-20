defmodule AoC22.Day20.B do
  alias AoC22.Utils

  @decryption_key 811_589_153
  @iterations 10

  def solve(input) do
    indexed_list =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&String.to_integer/1)
      |> Enum.map(&(&1 * @decryption_key))
      |> Enum.with_index()

    duplicated_indexed_list = indexed_list |> List.duplicate(@iterations) |> List.flatten()

    list_length = length(indexed_list)

    resulting_list =
      duplicated_indexed_list
      |> Enum.reduce(indexed_list, fn indexed_values, acc ->
        move(indexed_values, acc, list_length)
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
