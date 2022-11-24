defmodule Aoc19.Day2b do
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

    try do
      for i <- 1..100 do
        for j <- 1..100 do
          _ =
            case result(opcode, i, j) do
              19_690_720 ->
                throw(100 * i + j)

              _ ->
                nil
            end
        end
      end
    catch
      result -> result
    end
  end

  defp result(opcode, noun, verb) do
    opcode = replace(opcode, noun, verb)

    opcode
    |> intcode(opcode, 0)
    |> Enum.at(0)
  end

  defp verify([x | _] = opcode) when x in @opcode, do: opcode

  defp replace(opcode, noun, verb) do
    opcode
    |> List.update_at(1, fn _ -> noun end)
    |> List.update_at(2, fn _ -> verb end)
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
