defmodule Aoc19.Day8a do
  @moduledoc false

  @wide 25
  @tall 6

  def start(input_location) do
    layer =
      input_location
      |> read()
      |> layers()
      |> get_layer_with_least(0)

    ones = count(layer, 1)
    twos = count(layer, 2)

    ones * twos
  end

  defp get_layer_with_least(layers, number) do
    layers
    |> Enum.reduce({[], @wide * @tall}, &count_layer(&1, &2, number))
    |> elem(0)
  end

  defp count_layer(current_layer, {min_layer, min_count}, number) do
    current_count = count(current_layer, number)
    get_lowest({current_layer, current_count}, {min_layer, min_count})
  end

  defp count(layer, number), do: Enum.count(layer, fn x -> x == number end)

  defp get_lowest({_, count1} = l1, {_, count2}) when count1 < count2 do
    l1
  end

  defp get_lowest(_, {_, _} = l2), do: l2

  defp layers(digits) do
    Enum.chunk_every(digits, @wide * @tall)
  end

  defp read(input_location) do
    input_location
    |> File.read!()
    |> String.graphemes()
    |> Enum.reject(fn x -> x == "\n" end)
    |> Enum.map(&String.to_integer/1)
  end
end
