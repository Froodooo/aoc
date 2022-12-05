defmodule AoC22.Day5.Parse do
  def parse_stacks(stacks) do
    stacks
    |> String.split("\n")
    |> remove_last()
    |> Enum.map(&String.codepoints/1)
    |> Enum.map(&Enum.chunk_every(&1, 4))
    |> Enum.map(&normalize_crates/1)
    |> create_stacks()
  end

  def parse_instructions(instructions) do
    instructions
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&(Regex.scan(~r/move (\d+) from (\d+) to (\d+)/, &1) |> Enum.at(0)))
    |> Enum.map(&remove_first/1)
    |> Enum.map(&parse_instruction/1)
  end

  defp update_stacks_map(stacks_map, _index, []), do: stacks_map

  defp update_stacks_map(stacks_map, index, crate) do
    case Map.get(stacks_map, index) do
      nil -> Map.put(stacks_map, index, [crate])
      _ -> Map.update!(stacks_map, index, fn x -> x ++ [crate] end)
    end
  end

  defp normalize_crates(crates) do
    Enum.map(crates, &normalize_crate/1)
  end

  defp normalize_crate([" ", " ", " ", " "]), do: []
  defp normalize_crate([" ", " ", " "]), do: []
  defp normalize_crate(crate), do: Enum.at(crate, 1)

  defp create_stacks(raw_stacks) do
    stacks_map = Map.new()

    stacks_map =
      Enum.reduce(raw_stacks, stacks_map, fn stack_line, stacks_map ->
        stack_line_indexed = Enum.with_index(stack_line, 1)

        Enum.reduce(stack_line_indexed, stacks_map, fn {crate, index}, stacks_map ->
          update_stacks_map(stacks_map, index, crate)
        end)
      end)

    stacks_map
  end

  defp remove_last(stacks) do
    stacks
    |> Enum.reverse()
    |> tl()
    |> Enum.reverse()
  end

  defp remove_first(instructions), do: tl(instructions)

  defp parse_instruction(instruction), do: Enum.map(instruction, &String.to_integer/1)
end
