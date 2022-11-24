defmodule Aoc19.Day9a do
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
  @relative_base 9
  @halt 99

  @boost_input 1

  def start(input_location) do
    opcode = Common.read_numbers(input_location, ",")

    send(self(), {:output, 0})
    send(self(), {:relative_base, 0})
    intcode(opcode, opcode, 0)

    receive_relative_base()
    receive_output()
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
         [mode1, mode2, mode3],
         [param1, param2, result | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)
    {opcode, value2} = get_value(mode2, param2, opcode)
    result = get_input_index(mode3, result)
    opcode = expand_opcode(opcode, result)

    opcode =
      List.update_at(opcode, result, fn _ ->
        value1 + value2
      end)

    index = update_index(index, get_update_length(@add))
    {opcode, index}
  end

  defp do_operation(
         @multiply,
         [mode1, mode2, mode3],
         [param1, param2, result | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)
    {opcode, value2} = get_value(mode2, param2, opcode)
    result = get_input_index(mode3, result)
    opcode = expand_opcode(opcode, result)

    opcode =
      List.update_at(opcode, result, fn _ ->
        value1 * value2
      end)

    index = update_index(index, get_update_length(@multiply))
    {opcode, index}
  end

  defp do_operation(@input, [mode1 | _], [param1 | _], opcode, index) do
    param1 = get_input_index(mode1, param1)

    opcode = List.update_at(opcode, param1, fn _ -> @boost_input end)
    index = update_index(index, get_update_length(@input))

    {opcode, index}
  end

  defp do_operation(@output, [mode1 | _], [param1 | _], opcode, index) do
    {opcode, value1} = get_value(mode1, param1, opcode)

    receive_output()
    send(self(), {:output, value1})

    index = update_index(index, get_update_length(@output))
    {opcode, index}
  end

  defp do_operation(
         @jump_if_true,
         [mode1, mode2 | _],
         [param1, param2 | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)
    {opcode, value2} = get_value(mode2, param2, opcode)

    index =
      if value1 != 0,
        do: value2,
        else: update_index(index, get_update_length(@jump_if_true))

    {opcode, index}
  end

  defp do_operation(
         @jump_if_false,
         [mode1, mode2 | _],
         [param1, param2 | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)
    {opcode, value2} = get_value(mode2, param2, opcode)

    index =
      if value1 == 0,
        do: value2,
        else: update_index(index, get_update_length(@jump_if_true))

    {opcode, index}
  end

  defp do_operation(
         @less_than,
         [mode1, mode2, mode3],
         [param1, param2, param3 | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)
    {opcode, value2} = get_value(mode2, param2, opcode)
    param3 = get_input_index(mode3, param3)
    opcode = expand_opcode(opcode, param3)

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
         [mode1, mode2, mode3],
         [param1, param2, param3 | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)
    {opcode, value2} = get_value(mode2, param2, opcode)
    param3 = get_input_index(mode3, param3)
    opcode = expand_opcode(opcode, param3)

    value = if value1 == value2, do: 1, else: 0

    opcode =
      List.update_at(opcode, param3, fn _ ->
        value
      end)

    index = update_index(index, get_update_length(@equals))
    {opcode, index}
  end

  defp do_operation(
         @relative_base,
         [mode1 | _],
         [param1 | _],
         opcode,
         index
       ) do
    {opcode, value1} = get_value(mode1, param1, opcode)

    relative_base = receive_relative_base() + value1
    send(self(), {:relative_base, relative_base})

    index = update_index(index, get_update_length(@relative_base))

    {opcode, index}
  end

  defp update_index(index, increase), do: index + increase

  defp update_modes(modes) do
    case length(modes) do
      0 -> [0, 0, 0]
      1 -> Enum.concat(modes, [0, 0])
      2 -> Enum.concat(modes, [0])
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

  defp receive_output() do
    receive do
      {:output, value} -> value
    end
  end

  defp receive_relative_base() do
    receive do
      {:relative_base, value} -> value
    end
  end

  defp get_value(0, value, opcode) when length(opcode) <= value do
    opcode = expand_opcode(opcode, value)
    get_value(0, value, opcode)
  end

  defp get_value(0, value, opcode), do: {opcode, Enum.at(opcode, value)}
  defp get_value(1, value, opcode), do: {opcode, value}

  defp get_value(2, value, opcode) do
    relative_base = receive_relative_base()
    send(self(), {:relative_base, relative_base})
    value = relative_base + value
    get_value(0, value, opcode)
  end

  defp get_input_index(0, value), do: value
  defp get_input_index(1, value), do: value

  defp get_input_index(2, value) do
    relative_base = receive_relative_base()
    send(self(), {:relative_base, relative_base})
    relative_base + value
  end

  defp expand_opcode(opcode, value) when length(opcode) <= value do
    length = value - length(opcode) + 1
    suffix = List.duplicate(0, length)
    Enum.concat(opcode, suffix)
  end

  defp expand_opcode(opcode, _value), do: opcode

  defp get_update_length(@add), do: 4
  defp get_update_length(@multiply), do: 4
  defp get_update_length(@input), do: 2
  defp get_update_length(@output), do: 2
  defp get_update_length(@jump_if_true), do: 3
  defp get_update_length(@jump_if_false), do: 3
  defp get_update_length(@less_than), do: 4
  defp get_update_length(@equals), do: 4
  defp get_update_length(@relative_base), do: 2
end
