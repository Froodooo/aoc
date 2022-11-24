defmodule Aoc19.Day2a do
  @moduledoc false

  alias Aoc19.Utils.Common

  @add 1
  @multiply 2
  @halt 99
  @opcode [@add, @multiply, @halt]

  def start(input_location) do
    opcode =
      input_location
      |> Common.read_numbers(",")
      |> verify()
      |> replace()

    opcode
    |> intcode(opcode, 0)
    |> Enum.at(0)
  end

  defp verify([x | _] = opcode) when x in @opcode, do: opcode

  defp replace(opcode) do
    opcode
    |> List.update_at(1, fn _ -> 12 end)
    |> List.update_at(2, fn _ -> 2 end)
  end

  defp intcode([@halt | _], opcode, _), do: opcode

  defp intcode([@add, int1, int2, result | _], opcode, index) do
    opcode =
      List.update_at(opcode, result, fn _ ->
        Enum.at(opcode, int1) + Enum.at(opcode, int2)
      end)

    index = index + 4
    {_, rest} = Enum.split(opcode, index)

    intcode(rest, opcode, index)
  end

  defp intcode([@multiply, int1, int2, result | _], opcode, index) do
    opcode =
      List.update_at(opcode, result, fn _ ->
        Enum.at(opcode, int1) * Enum.at(opcode, int2)
      end)

    index = index + 4
    {_, rest} = Enum.split(opcode, index)

    intcode(rest, opcode, index)
  end
end
