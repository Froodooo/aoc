defmodule AoC22.Day5.Parse do
  @first_crate_offset 1
  @instruction_regex ~r/move (\d+) from (\d+) to (\d+)/
  @raw_crate_size 4
  @space " "

  def parse_stacks(stacks) do
    stacks
    |> String.split("\n")
    |> Enum.drop(-1)
    |> Enum.map(&String.codepoints/1)
    |> Enum.map(&Enum.chunk_every(&1, @raw_crate_size))
    |> Enum.map(&normalize_crates/1)
    |> create_stacks()
  end

  def parse_instructions(instructions) do
    instructions
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&(Regex.scan(@instruction_regex, &1) |> hd()))
    |> Enum.map(&tl/1)
    |> Enum.map(&parse_instruction/1)
  end

  defp normalize_crates(crates), do: Enum.map(crates, &normalize_crate/1)

  defp normalize_crate(crate) do
    cond do
      empty_crate?(crate) -> []
      true -> Enum.at(crate, 1)
    end
  end

  defp empty_crate?(crate), do: Enum.all?(crate, &(&1 == @space))

  defp create_stacks(raw_stacks) do
    Enum.reduce(raw_stacks, Map.new(), &stack_line/2)
  end

  defp stack_line(stack_line, stacks_map) do
    stack_line
    |> Enum.with_index(@first_crate_offset)
    |> Enum.reduce(stacks_map, &stack_crate/2)
  end

  defp stack_crate({crate, index}, stacks_map) do
    update_stacks_map(stacks_map, index, crate)
  end

  defp update_stacks_map(stacks_map, _index, []), do: stacks_map

  defp update_stacks_map(stacks_map, index, crate) do
    case Map.get(stacks_map, index) do
      nil -> Map.put(stacks_map, index, [crate])
      _ -> Map.update!(stacks_map, index, fn x -> x ++ [crate] end)
    end
  end

  defp parse_instruction(instruction), do: Enum.map(instruction, &String.to_integer/1)
end
