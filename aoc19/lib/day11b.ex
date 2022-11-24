defmodule Aoc19.Day11b do
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

  @left 0
  @right 1

  @black 0
  @white 1

  def start(input_location, print? \\ false) do
    opcode = Common.read_numbers(input_location, ",")

    send(self(), {:relative_base, 0})

    first_panel = {{0, 0}, @white}

    panels =
      opcode
      |> move(0, {0, 0}, :up, [first_panel])
      |> normalize()

    if print?, do: paint(panels), else: Enum.count(panels)
  end

  defp normalize(panels) do
    Enum.map(panels, fn {{x, y}, color} -> {{abs(x), abs(y)}, color} end)
  end

  defp paint(panels) do
    panels
    |> Enum.sort_by(fn {{_x, y}, _color} -> y end)
    |> Enum.group_by(fn {{_x, y}, _color} -> y end)
    |> Map.to_list()
    |> Enum.map(&paint_row/1)

    :ok
  end

  defp paint_row({_row, coordinates}) do
    coordinates
    |> fill()
    |> Enum.sort_by(fn {{x, _y}, _color} -> x end)
    |> Enum.map(fn {_coordinate, color} -> paint_color(color) end)
    |> Enum.join()
    |> IO.puts()
  end

  defp fill(coordinates) do
    {{_x, y}, _color} = List.first(coordinates)
    Enum.reduce(0..42, coordinates, fn counter, coordinates ->
      case Enum.find(coordinates, nil, fn {{x, _y}, _color} -> x == counter end) do
        nil -> [{{counter, y}, @black} | coordinates]
        _ -> coordinates
      end
    end)
  end

  defp paint_color(@black), do: "⬛"
  defp paint_color(@white), do: "⬜"

  defp move(opcode, index, location, direction, panels) do
    send_location_input(location, panels)
    rest = rest(opcode, index)

    case intcode(rest, opcode, index) do
      {color, opcode, index} ->
        panels = update_panels(panels, location, color)

        rest = rest(opcode, index)
        {turn, opcode, index} = intcode(rest, opcode, index)

        location = location(location, direction, turn)
        direction = direction(direction, turn)

        move(opcode, index, location, direction, panels)

      _ ->
        receive_relative_base()
        receive_input()
        panels
    end
  end

  defp update_panels(panels, location, color) do
    existing_panel =
      Enum.find(panels, fn {panel, _color} -> panel == location end)

    panels =
      if existing_panel != nil,
        do: List.delete(panels, existing_panel),
        else: panels

    [{location, color} | panels]
  end

  defp send_location_input(location, panels) do
    input =
      case Enum.find(panels, fn {panel, _color} -> panel == location end) do
        {_location, color} -> color
        _ -> @black
      end

    send(self(), {:input, input})
  end

  defp location({x, y}, :up, @left), do: {x - 1, y}
  defp location({x, y}, :down, @left), do: {x + 1, y}
  defp location({x, y}, :left, @left), do: {x, y - 1}
  defp location({x, y}, :right, @left), do: {x, y + 1}

  defp location({x, y}, :up, @right), do: {x + 1, y}
  defp location({x, y}, :down, @right), do: {x - 1, y}
  defp location({x, y}, :left, @right), do: {x, y + 1}
  defp location({x, y}, :right, @right), do: {x, y - 1}

  defp direction(:up, @left), do: :left
  defp direction(:down, @left), do: :right
  defp direction(:left, @left), do: :down
  defp direction(:right, @left), do: :up

  defp direction(:up, @right), do: :right
  defp direction(:down, @right), do: :left
  defp direction(:left, @right), do: :up
  defp direction(:right, @right), do: :down

  defp intcode([@halt | _], opcode, _), do: opcode

  defp intcode([next | rest], opcode, index) do
    [code, _ | modes] =
      next
      |> update_next()
      |> Enum.reverse()

    modes = update_modes(modes)
    {opcode, index} = do_operation(code, modes, rest, opcode, index)
    rest = rest(opcode, index)

    if code == @output do
      {receive_output(), opcode, index}
    else
      intcode(rest, opcode, index)
    end
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

    opcode = List.update_at(opcode, param1, fn _ -> receive_input() end)
    # send(self(), {:input, 0})
    index = update_index(index, get_update_length(@input))

    {opcode, index}
  end

  defp do_operation(@output, [mode1 | _], [param1 | _], opcode, index) do
    {opcode, value1} = get_value(mode1, param1, opcode)

    # receive_output()
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

  defp receive_input() do
    receive do
      {:input, value} -> value
    end
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
