defmodule Aoc19.Day10a do
  alias Aoc19.Utils.Common

  @asteroid "#"

  def start(input_location) do
    input_location
    |> read()
    |> gradients()
    |> Enum.map(fn {_asteroid, visible} -> visible end)
    |> Enum.map(fn visible -> Enum.count(visible) end)
    |> Enum.max()
  end

  defp gradients(asteroids) do
    Enum.map(asteroids, &calculate_gradients(&1, asteroids))
  end

  defp calculate_gradients(asteroid, asteroids) do
    {asteroid,
     asteroids
     |> Enum.reject(fn x -> x == asteroid end)
     |> Enum.map(&calculate_gradient(asteroid, &1))
     |> Enum.uniq()}
  end

  defp calculate_gradient({x, y}, {a, b}) when x == a do
    cond do
      y - b > 0 -> :row_up
      y - b < 0 -> :row_down
    end
  end

  defp calculate_gradient({x, y}, {a, b}) when y == b do
    cond do
      x - a > 0 -> :column_left
      x - a < 0 -> :column_right
    end
  end

  defp calculate_gradient({x, y}, {a, b}) do
    x = x - a
    y = y - b
    gcd = Integer.gcd(x, y)
    {x / gcd, y / gcd}
  end

  defp read(input_location) do
    input_location
    |> Common.read()
    |> Enum.with_index()
    |> Enum.flat_map(&read_row/1)
  end

  defp read_row({row, y}) do
    row
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.map(&read_column(&1, y))
    |> Enum.reject(&is_nil?/1)
  end

  defp read_column({@asteroid, x}, y), do: {x, y}
  defp read_column(_, _), do: nil

  defp is_nil?(nil), do: true
  defp is_nil?(_), do: false
end
