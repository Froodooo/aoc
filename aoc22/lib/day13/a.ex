defmodule AoC22.Day13.A do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n\n")
    |> Enum.map(&String.split/1)
    |> Enum.map(&eval_pair/1)
    |> Enum.map(&zip/1)
    |> Enum.with_index(1)
    |> Enum.map(&compare/1)
    |> Enum.sum()
  end

  defp eval_pair(pair) do
    pair
    |> Enum.map(&Code.eval_string/1)
    |> Enum.map(&elem(&1, 0))
  end

  defp compare({pairs, index}) do
    Enum.reduce_while(pairs, 0, fn {p1, p2}, acc ->
      cond do
        p1 < p2 -> {:halt, index}
        p1 > p2 -> {:halt, 0}
        true -> {:cont, acc}
      end
    end)
  end

  defp normalize([packet1, packet2]) do
    case [packet1, packet2] do
      [_, [-1]] -> [[0], [-1]]
      [[-1], _] -> [[-1], [0]]
      _ -> [packet1, packet2]
    end
  end

  defp equalize([packet1, packet2]) do
    cond do
      length(packet1) > length(packet2) ->
        [packet1, packet2 ++ List.duplicate(-1, length(packet1) - length(packet2))]

      length(packet2) > length(packet1) ->
        [packet1 ++ List.duplicate(-1, length(packet2) - length(packet1)), packet2]

      true ->
        [packet1, packet2]
    end
  end

  defp zip([packet1, packet2]), do: zip(packet1, packet2)

  defp zip(packet1, packet2) do
    [packet1, packet2] = [packet1, packet2] |> normalize() |> equalize()
    zipped = Enum.zip(packet1, packet2)

    Enum.map(zipped, fn {z1, z2} ->
      cond do
        is_list(z1) and is_number(z2) -> zip(z1, [z2])
        is_list(z2) and is_number(z1) -> zip([z1], z2)
        is_list(z1) and is_list(z2) -> zip(z1, z2)
        true -> {z1, z2}
      end
    end)
    |> List.flatten()
  end
end
