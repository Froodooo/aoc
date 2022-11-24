defmodule Aoc19.Day5a do
  @moduledoc false

  alias Aoc19.Utils.Common

  @add 1
  @multiply 2
  @input 3
  @output 4
  @halt 99
  @opcode [@add, @multiply, @input, @output, @halt]

  @air_condition_unit_id 1

  def start(input_location) do
    opcode =
      input_location
      |> Common.read_numbers(",")
      |> verify()

    send(self(), 0)

    intcode(opcode, opcode, 0)
    receive_value()
  end

  defp verify([x | _] = opcode) when x in @opcode, do: opcode

  defp intcode([@halt | _], opcode, _), do: opcode

  defp intcode([@add, index1, index2, result | _], opcode, index) do
    opcode =
      List.update_at(opcode, result, fn _ ->
        value1 = Enum.at(opcode, index1)
        value2 = Enum.at(opcode, index2)
        value1 + value2
      end)

    index = update_index(index, 4)
    rest = rest(opcode, index)

    intcode(rest, opcode, index)
  end

  defp intcode([@multiply, index1, index2, result | _], opcode, index) do
    opcode =
      List.update_at(opcode, result, fn _ ->
        value1 = Enum.at(opcode, index1)
        value2 = Enum.at(opcode, index2)
        value1 * value2
      end)

    index = update_index(index, 4)
    rest = rest(opcode, index)

    intcode(rest, opcode, index)
  end

  defp intcode([@input, index1 | _], opcode, index) do
    opcode =
      List.update_at(opcode, index1, fn _ ->
        @air_condition_unit_id
      end)

    index = update_index(index, 2)
    rest = rest(opcode, index)

    intcode(rest, opcode, index)
  end

  defp intcode([@output, index1 | _], opcode, index) do
    receive_value()
    send(self(), Enum.at(opcode, index1))

    index = update_index(index, 2)
    rest = rest(opcode, index)

    intcode(rest, opcode, index)
  end

  defp intcode([next | rest], opcode, index) do
    [code, _ | modes] =
      next
      |> Integer.digits()
      |> Enum.reverse()

    opcode = do_operation(code, modes, rest, opcode)
    index = update_index(index, get_update_length(code))
    rest = rest(opcode, index)

    intcode(rest, opcode, index)
  end

  defp get_update_length(@add), do: 4
  defp get_update_length(@multiply), do: 4
  defp get_update_length(@output), do: 2

  defp do_operation(@add, modes, [number1, number2, result | _], opcode) do
    [mode1, mode2] = update_modes(modes)
    value1 = get_value(mode1, number1, opcode)
    value2 = get_value(mode2, number2, opcode)

    List.update_at(opcode, result, fn _ ->
      value1 + value2
    end)
  end

  defp do_operation(@multiply, modes, [number1, number2, result | _], opcode) do
    [mode1, mode2] = update_modes(modes)
    value1 = get_value(mode1, number1, opcode)
    value2 = get_value(mode2, number2, opcode)

    List.update_at(opcode, result, fn _ ->
      value1 * value2
    end)
  end

  defp do_operation(@output, modes, [number1 | _], opcode) do
    [mode1] = modes
    value1 = get_value(mode1, number1, opcode)

    receive_value()
    send(self(), value1)

    opcode
  end

  defp get_value(0, value, opcode), do: Enum.at(opcode, value)
  defp get_value(1, value, _opcode), do: value

  defp update_modes(modes) do
    case length(modes) do
      0 -> [0, 0 | modes] |> Enum.reverse()
      1 -> [0 | modes] |> Enum.reverse()
      _ -> modes
    end
  end

  defp update_index(index, increase), do: index + increase

  defp rest(opcode, index) do
    {_, rest} = Enum.split(opcode, index)
    rest
  end

  defp receive_value() do
    receive do
      value -> value
    end
  end
end
