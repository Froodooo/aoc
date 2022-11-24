defmodule Aoc19.Day4b do
  @moduledoc false

  alias Aoc19.Utils.Common

  def start(input_location) do
    [lower, upper] = Common.read_numbers(input_location, "-")

    check(lower, upper, 0)
  end

  defp check(current, upper, count) when current <= upper do
    with :ok <- adjacent?(current),
         :ok <- increasing?(current) do
      check(current + 1, upper, count + 1)
    else
      _ -> check(current + 1, upper, count)
    end
  end

  defp check(_, _, count), do: count

  defp increasing?(current) do
    current
    |> Integer.to_string()
    |> String.graphemes()
    |> is_increasing?()
  end

  defp is_increasing?([]), do: :ok
  defp is_increasing?([_]), do: :ok

  defp is_increasing?([h1, h2 | rest]) when h1 <= h2 do
    is_increasing?([h2 | rest])
  end

  defp is_increasing?(_), do: :error

  defp adjacent?(current) do
    current
    |> Integer.to_string()
    |> String.graphemes()
    |> is_adjacent?()
  end

  defp is_adjacent?([]), do: :error

  defp is_adjacent?([h1, h1, h1 | rest]) do
    rest = skip(h1, rest)
    is_adjacent?(rest)
  end

  defp is_adjacent?([h1, h1 | _rest]), do: :ok
  defp is_adjacent?([_h1 | rest]), do: is_adjacent?(rest)

  defp skip(h, [h | rest]), do: skip(h, rest)
  defp skip(_h, rest), do: rest
end
