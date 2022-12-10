defmodule AoC22.Day10.B do
  alias AoC22.Utils
  alias AoC22.Day10.Matrix

  @register_start 1
  @cycle_start 0

  def solve(input) do
    crt = initialize_crt()

    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
    |> Enum.reduce({crt, @register_start, @cycle_start}, &run(&1, &2))
    |> elem(0)
    |> print()
  end

  defp print(matrix) do
    list = Matrix.to_list(matrix)

    Enum.each(0..(length(list) - 1), fn y ->
      0..(length(Enum.at(list, 0)) - 1)
      |> Enum.reduce([], fn x, row ->
        [matrix[y][x] | row]
      end)
      |> Enum.reverse()
      |> Enum.join()
      |> IO.puts()
    end)
  end

  defp initialize_crt() do
    nil |> List.duplicate(40) |> List.duplicate(6) |> Matrix.from_list()
  end

  defp parse_line(line) do
    case String.split(line) do
      [instruction, value] -> [instruction, String.to_integer(value)]
      instruction -> instruction
    end
  end

  defp run(instruction, acc, inner_cycle \\ 1, do_sum \\ True)

  defp run(["noop"], {crt, register, cycle}, _inner_cycle, _do_sum) do
    {update_crt(crt, register, cycle), register, cycle + 1}
  end

  defp run(["addx", value], {crt, register, cycle}, inner_cycle, _do_sum) when inner_cycle < 2 do
    run(["addx", value], {update_crt(crt, register, cycle), register, cycle + 1}, inner_cycle + 1)
  end

  defp run(["addx", value], {crt, register, cycle}, _inner_cycle, _do_sum) do
    {update_crt(crt, register, cycle), register + value, cycle + 1}
  end

  defp update_crt(crt, register, cycle) do
    put_pixel(crt, register, trunc(cycle / 40), current_pixel(cycle))
  end

  defp current_pixel(cycle), do: rem(cycle, 40)

  defp put_pixel(crt, register, row, pixel) do
    if register in (pixel - 1)..(pixel + 1) do
      put_in(crt[row][pixel], "⬛")
    else
      put_in(crt[row][pixel], "⬜")
    end
  end
end
