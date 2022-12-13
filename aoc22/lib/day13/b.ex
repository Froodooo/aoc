defmodule AoC22.Day13.B do
  alias AoC22.Utils

  def solve(input) do
    input
    |> Utils.input()
    |> String.replace("\n\n", "\n")
    |> String.split("\n")
    |> Enum.map(&eval_packet/1)
    |> Enum.concat([[[2]]])
    |> Enum.concat([[[6]]])
    |> bubble_sort()
    |> Enum.with_index(1)
    |> Enum.filter(&divider?/1)
    |> Enum.map(&elem(&1, 1))
    |> Enum.product()
  end

  defp eval_packet(packet) do
    packet
    |> Code.eval_string()
    |> elem(0)
  end

  defp compare([]), do: false

  defp compare(pairs) do
    Enum.reduce_while(pairs, true, fn {p1, p2}, acc ->
      cond do
        p1 < p2 -> {:halt, true}
        p1 > p2 -> {:halt, false}
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

  defp bubble_sort([first | packets]) do
    {result, changed?} = Enum.reduce(packets, {[first], false}, &do_bubble_sort/2)

    case changed? do
      true -> result |> Enum.reverse() |> bubble_sort()
      false -> Enum.reverse(result)
    end
  end

  defp do_bubble_sort(current, {[previous | rest], changed?}) do
    in_order? =
      previous
      |> zip(current)
      |> compare()

    case in_order? do
      true -> {[current, previous | rest], if(changed?, do: changed?, else: false)}
      false -> {[previous, current | rest], true}
    end
  end

  defp divider?({packet, _}) when packet == [[2]], do: true
  defp divider?({packet, _}) when packet == [[6]], do: true
  defp divider?(_), do: false
end
