defmodule Aoc19.Day10b do
  alias Aoc19.Utils.Common

  @asteroid "#"

  def start(input_location) do
    input = read(input_location)

    {best, _detected} =
      input
      |> gradients()
      |> Enum.map(fn {asteroid, visible} -> {asteroid, Enum.count(visible)} end)
      |> Enum.max_by(fn {_asteroid, count} -> count end)

    vaporized =
    best
    |> calculate_gradients(input, false)
    |> sort()
    |> vaporize(best)

    {x, y} = Enum.at(vaporized, 199)
    x * 100 + y
  end

  defp vaporize(gradients, best, vaporized \\ []) do
    {left_gradients, vaporized} = 
    Enum.map_reduce(gradients, vaporized, &vaporize_gradient(&1, &2, best))

    continue({left_gradients, vaporized}, best)
  end

  defp continue({left_gradients, vaporized}, best) do
    case Enum.all?(left_gradients, fn gradient -> gradient == nil end) do
      true -> Enum.reverse(vaporized)
      _ -> vaporize(left_gradients, best, vaporized)
    end
  end

  defp vaporize_gradient(nil, vaporized, _best), do: {nil, vaporized}

  defp vaporize_gradient({_gradient, [asteroid]}, vaporized, _best) do
    {nil, [asteroid | vaporized]}
  end

  defp vaporize_gradient({gradient, asteroids}, vaporized, best) do
    closest = closest(asteroids, best)
    asteroids = List.delete(asteroids, closest)
    {{gradient, asteroids}, [closest | vaporized]}
  end

  defp closest(asteroids, {x, y}) do
    closest_distance_index =
      asteroids
      |> Enum.with_index()
      |> Enum.map(fn {{a, b}, index} -> {{abs(x - a) + abs(y - b)}, index} end)
      |> Enum.max_by(fn {distance, _index} -> distance end)
      |> elem(1)

    Enum.at(asteroids, closest_distance_index)
  end

  defp sort({_best_asteroid, gradients}) do
    gradients
    |> Enum.sort_by(fn {_asteroid, found_gradients} -> found_gradients end)
    |> Enum.map(fn {asteroid, gradient} -> {gradient, asteroid} end)
    |> Enum.group_by(fn {gradient, _asteroid} -> gradient end, fn {_gradient,
                                                                   asteroid} ->
      asteroid
    end)
    |> Map.to_list()
    |> Enum.sort_by(fn {gradient, _asteroids} -> gradient end)
  end

  defp gradients(asteroids) do
    Enum.map(asteroids, &calculate_gradients(&1, asteroids, true))
  end

  defp calculate_gradients(asteroid, asteroids, uniq?) do
    gradients =
      asteroids
      |> Enum.reject(fn x -> x == asteroid end)
      |> Enum.map(&calculate_gradient(asteroid, &1))
      |> uniq_gradient(uniq?)

    {asteroid, gradients}
  end

  defp uniq_gradient(gradients, true) do
    Enum.uniq_by(gradients, fn {_asteroid, gradient} -> gradient end)
  end

  defp uniq_gradient(gradients, false), do: gradients

  defp calculate_gradient({x, y}, {a, b}) do
    delta_x = a - x
    delta_y = y - b
    gradient = :math.atan2(delta_x, delta_y) * 180 / :math.pi()
    gradient = normalize(gradient)
    {{a, b}, gradient}
  end

  defp normalize(gradient) when gradient < 0, do: 360 + gradient
  defp normalize(gradient), do: gradient

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
