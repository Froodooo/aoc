defmodule Aoc19.Day5b do
  @moduledoc false

  alias Aoc19.Utils.Common

  @add 1
  @multiply 2
  @input 3
  @output 4
  @jump_if_true 5
  @jump_if_false 6
  @less_than 7
  @equals 8
  @halt 99

  @air_condition_unit_id 5

  def start(input_location) do
    opcode =
      input_location
      |> Common.read_numbers(",")

    send(self(), 0)
    intcode(opcode, opcode, 0)
    receive_value()
  end

  defp intcode([@halt | _], opcode, _), do: opcode

  defp intcode([next | rest], opcode, index) do
    [code, _ | modes] =
      next
      |> update_next()
      |> Enum.reverse()

    modes = update_modes(modes)
    {opcode, index} = do_operation(code, modes, rest, opcode, index)
    rest = rest(opcode, index)

    intcode(rest, opcode, index)
  end

  defp do_operation(
         @add,
         [mode1, mode2],
         [number1, number2, result | _],
         opcode,
         index
       ) do
    value1 = get_value(mode1, number1, opcode)
    value2 = get_value(mode2, number2, opcode)

    opcode =
      List.update_at(opcode, result, fn _ ->
        value1 + value2
      end)

    index = update_index(index, get_update_length(@add))
    {opcode, index}
  end

  defp do_operation(
         @multiply,
         [mode1, mode2],
         [number1, number2, result | _],
         opcode,
         index
       ) do
    value1 = get_value(mode1, number1, opcode)
    value2 = get_value(mode2, number2, opcode)

    opcode =
      List.update_at(opcode, result, fn _ ->
        value1 * value2
      end)

    index = update_index(index, get_update_length(@multiply))
    {opcode, index}
  end

  defp do_operation(@input, _modes, [number1 | _], opcode, index) do
    opcode =
      List.update_at(opcode, number1, fn _ ->
        @air_condition_unit_id
      end)

    index = update_index(index, get_update_length(@input))

    {opcode, index}
  end

  defp do_operation(@output, [mode1, _], [number1 | _], opcode, index) do
    value1 = get_value(mode1, number1, opcode)

    receive_value()
    send(self(), value1)

    index = update_index(index, get_update_length(@output))
    {opcode, index}
  end

  defp do_operation(
         @jump_if_true,
         [mode1, mode2],
         [param1, param2 | _],
         opcode,
         index
       ) do
    value1 = get_value(mode1, param1, opcode)
    value2 = get_value(mode2, param2, opcode)

    index =
      if value1 != 0,
        do: value2,
        else: update_index(index, get_update_length(@jump_if_true))

    {opcode, index}
  end

  defp do_operation(
         @jump_if_false,
         [mode1, mode2],
         [param1, param2 | _],
         opcode,
         index
       ) do
    value1 = get_value(mode1, param1, opcode)
    value2 = get_value(mode2, param2, opcode)

    index =
      if value1 == 0,
        do: value2,
        else: update_index(index, get_update_length(@jump_if_true))

    {opcode, index}
  end

  defp do_operation(
         @less_than,
         [mode1, mode2],
         [param1, param2, param3 | _],
         opcode,
         index
       ) do
    value1 = get_value(mode1, param1, opcode)
    value2 = get_value(mode2, param2, opcode)

    value = if value1 < value2, do: 1, else: 0

    opcode =
      List.update_at(opcode, param3, fn _ ->
        value
      end)

    index = update_index(index, get_update_length(@less_than))
    {opcode, index}
  end

  defp do_operation(
         @equals,
         [mode1, mode2],
         [param1, param2, param3 | _],
         opcode,
         index
       ) do
    value1 = get_value(mode1, param1, opcode)
    value2 = get_value(mode2, param2, opcode)

    value = if value1 == value2, do: 1, else: 0

    opcode =
      List.update_at(opcode, param3, fn _ ->
        value
      end)

    index = update_index(index, get_update_length(@equals))
    {opcode, index}
  end

  defp update_index(index, increase), do: index + increase

  defp update_modes(modes) do
    case length(modes) do
      0 -> [0, 0 | modes] |> Enum.reverse()
      1 -> [0 | modes] |> Enum.reverse()
      _ -> modes
    end
  end

  defp update_next(next) do
    case Integer.digits(next) do
      [digit] -> [0, 0, 0, digit]
      digits -> digits
    end
  end

  defp rest(opcode, index) do
    {_, rest} = Enum.split(opcode, index)
    rest
  end

  defp receive_value() do
    receive do
      value -> value
    end
  end

  defp get_value(0, value, opcode), do: Enum.at(opcode, value)
  defp get_value(1, value, _opcode), do: value

  defp get_update_length(@add), do: 4
  defp get_update_length(@multiply), do: 4
  defp get_update_length(@input), do: 2
  defp get_update_length(@output), do: 2
  defp get_update_length(@jump_if_true), do: 3
  defp get_update_length(@jump_if_false), do: 3
  defp get_update_length(@less_than), do: 4
  defp get_update_length(@equals), do: 4
end
