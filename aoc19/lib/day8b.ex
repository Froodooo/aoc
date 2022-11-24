defmodule Aoc19.Day8b do
  @moduledoc false

  @wide 25
  @tall 6

  @black 0
  @white 1

  def start(input_location, print? \\ false) do
    input_location
    |> read()
    |> layers()
    |> build_message()
    |> print(print?)
  end

  defp print(message, false), do: Enum.join(message)

  defp print(message, true) do
    message
    |> Enum.map(&swap/1)
    |> Enum.chunk_every(@wide)
    |> Enum.map(&Enum.join/1)
    |> Enum.each(&IO.puts/1)
  end

  defp swap(0), do: " "
  defp swap(_), do: "■"

  defp build_message([first | layers]) do
    first
    |> Enum.with_index()
    |> Enum.map(&get_color(&1, layers))
  end

  defp get_color({color, _}, _) when color in [@black, @white] do
    color
  end

  defp get_color({_, index}, [layer | layers]) do
    layer
    |> Enum.with_index()
    |> Enum.at(index)
    |> get_color(layers)
  end

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
