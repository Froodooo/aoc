defmodule AoC22.Day17.A do
  alias AoC22.Utils

  @wall_left 0
  @wall_right 8
  @wall_bottom 0
  @rocks_stopped 2022

  def solve(input) do
    directions =
      input
      |> Utils.input()
      |> String.graphemes()

    emit_jet_gas(directions, MapSet.new(), 0, create_shape(0, 0), 0, 0, 0)
  end

  defp emit_jet_gas(_directions, _rocks, _shape_id, _shape, high_y, _iteration, fallen_rocks)
       when fallen_rocks == @rocks_stopped,
       do: high_y

  defp emit_jet_gas(directions, rocks, shape_id, shape, high_y, iteration, fallen_rocks) do
    direction = Enum.at(directions, rem(iteration, length(directions)))
    shape = push_shape(shape, direction, rocks)

    {fall_result, shape} = fall_shape(shape, rocks)
    new_shape_id = determine_shape_id(shape_id, fall_result)

    rocks = update_rocks(rocks, shape, shape_id, new_shape_id)

    high_y = update_high_y(high_y, rocks)

    fallen_rocks = update_fallen_rocks(fallen_rocks, shape_id, new_shape_id)

    shape = update_shape(shape, shape_id, new_shape_id, high_y)

    # if shape_id != new_shape_id do
    #   print(rocks, shape, high_y + 7)
    # end

    emit_jet_gas(directions, rocks, new_shape_id, shape, high_y, iteration + 1, fallen_rocks)
  end

  defp determine_shape_id(shape_id, :ok), do: shape_id
  defp determine_shape_id(shape_id, :not_moved), do: rem(shape_id + 1, 5)

  defp push_shape(shape, ">", rocks) do
    cond do
      Enum.any?(shape, fn {x, y} -> hits_wall?({x + 1, y}) or hits_rock?({x + 1, y}, rocks) end) ->
        shape

      true ->
        Enum.map(shape, fn {x, y} -> {x + 1, y} end)
    end
  end

  defp push_shape(shape, "<", rocks) do
    cond do
      Enum.any?(shape, fn {x, y} -> hits_wall?({x - 1, y}) or hits_rock?({x - 1, y}, rocks) end) ->
        shape

      true ->
        Enum.map(shape, fn {x, y} -> {x - 1, y} end)
    end
  end

  defp fall_shape(shape, rocks) do
    cond do
      Enum.any?(shape, fn {x, y} -> hits_wall?({x, y - 1}) or hits_rock?({x, y - 1}, rocks) end) ->
        {:not_moved, shape}

      true ->
        {:ok, Enum.map(shape, fn {x, y} -> {x, y - 1} end)}
    end
  end

  defp hits_wall?({x, y}), do: x == @wall_left or x == @wall_right or y == @wall_bottom

  defp hits_rock?({x, y}, rocks), do: MapSet.member?(rocks, {x, y})

  defp update_shape(shape, old_id, new_id, _high_y) when old_id == new_id, do: shape
  defp update_shape(_shape, _old_id, new_id, high_y), do: create_shape(new_id, high_y)

  defp update_rocks(rocks, shape, old_id, new_id) when old_id != new_id,
    do: MapSet.union(rocks, MapSet.new(shape))

  defp update_rocks(rocks, _shape, _old_id, _new_id), do: rocks

  defp update_high_y(high_y, rocks) do
    case MapSet.to_list(rocks) do
      [] -> high_y
      rocks_list -> rocks_list |> Enum.map(fn {_x, y} -> y end) |> Enum.max()
    end
  end

  defp update_fallen_rocks(fallen_rocks, old_id, new_id) when old_id != new_id,
    do: fallen_rocks + 1

  defp update_fallen_rocks(fallen_rocks, _old_id, _new_id), do: fallen_rocks

  defp create_shape(0, y), do: [{3, y + 4}, {4, y + 4}, {5, y + 4}, {6, y + 4}]
  defp create_shape(1, y), do: [{4, y + 4}, {3, y + 5}, {4, y + 5}, {5, y + 5}, {4, y + 6}]
  defp create_shape(2, y), do: [{3, y + 4}, {4, y + 4}, {5, y + 4}, {5, y + 5}, {5, y + 6}]
  defp create_shape(3, y), do: [{3, y + 4}, {3, y + 5}, {3, y + 6}, {3, y + 7}]
  defp create_shape(4, y), do: [{3, y + 4}, {4, y + 4}, {3, y + 5}, {4, y + 5}]

  # defp print(rocks, shape, high_y) do
  #   Enum.reduce(high_y..1, "", fn y, _acc ->
  #     Enum.reduce(@wall_left..@wall_right, "", fn x, acc ->
  #       if x == @wall_left or x == @wall_right do
  #         acc <> "|"
  #       else
  #         cond do
  #           MapSet.member?(rocks, {x, y}) -> acc <> "#"
  #           {x, y} in shape -> acc <> "@"
  #           true -> acc <> "."
  #         end
  #       end
  #     end) |> IO.puts()
  #   end)

  #   IO.puts("+-------+")
  # end
end
