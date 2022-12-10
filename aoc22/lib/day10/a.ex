defmodule AoC22.Day10.A do
  alias AoC22.Utils

  @sum_start 0
  @register_start 1
  @cycle_start 1
  @sum_cycles [20, 60, 100, 140, 180, 220]

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
    |> Enum.reduce({@sum_start, @register_start, @cycle_start}, &run(&1, &2))
    |> elem(0)
  end

  defp parse_line(line) do
    case String.split(line) do
      [instruction, value] -> [instruction, String.to_integer(value)]
      instruction -> instruction
    end
  end

  defp run(instruction, acc, inner_cycle \\ 1, do_sum \\ True)

  defp run(instruction, {signal_sum, register, cycle}, inner_cycle, do_sum)
       when do_sum == True and cycle in @sum_cycles do
    run(instruction, {signal_sum + register * cycle, register, cycle}, inner_cycle, False)
  end

  defp run(["noop"], {signal_sum, register, cycle}, _inner_cycle, _do_sum) do
    {signal_sum, register, cycle + 1}
  end

  defp run(["addx", value], {signal_sum, register, cycle}, inner_cycle, _do_sum)
       when inner_cycle < 2 do
    run(["addx", value], {signal_sum, register, cycle + 1}, inner_cycle + 1)
  end

  defp run(["addx", value], {signal_sum, register, cycle}, _inner_cycle, _do_sum) do
    {signal_sum, register + value, cycle + 1}
  end
end
