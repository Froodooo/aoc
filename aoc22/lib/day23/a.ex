defmodule AoC22.Day23.A do
  alias AoC22.Utils

  @proposals [:north, :south, :west, :east]
  @rounds 10

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&String.graphemes/1)
    |> parse()
    |> process(%{}, 0)
    |> empty()
  end

  defp empty(elves) do
    {min_x, _} = Enum.min_by(elves, &elem(&1, 0))
    {max_x, _} = Enum.max_by(elves, &elem(&1, 0))
    {_, min_y} = Enum.min_by(elves, &elem(&1, 1))
    {_, max_y} = Enum.max_by(elves, &elem(&1, 1))

    (abs(min_x) + abs(max_x) + 1) * (abs(min_y) + abs(max_y) + 1) - Enum.count(elves)
  end

  defp process(elves, _proposals, @rounds), do: elves

  defp process(elves, proposals, round) do
    proposals = round(elves, proposals, round)

    cond do
      proposals == %{} ->
        elves

      true ->
        elves = move_elves(elves, proposals)
        process(elves, %{}, round + 1)
    end
  end

  defp move_elves(elves, proposals) do
    Enum.reduce(proposals, elves, fn {{x, y}, elves_to_move}, elves ->
      case elves_to_move do
        [elve] -> [{x, y} | Enum.reject(elves, &(&1 == elve))]
        _ -> elves
      end
    end)
  end

  defp round(elves, proposals, round) do
    Enum.reduce(elves, proposals, fn elve, proposals ->
      case possible_moves(elve, elves) do
        [_, _, _, _] ->
          proposals

        moves ->
          case proposal(elve, moves, round) do
            {:ok, proposal} -> Map.update(proposals, proposal, [elve], &[elve | &1])
            {:no, _} -> proposals
          end
      end
    end)
  end

  defp possible_moves({x, y}, elves) do
    moves = []

    moves =
      if !Enum.member?(elves, {x, y - 1}) and !Enum.member?(elves, {x + 1, y - 1}) and
           !Enum.member?(elves, {x - 1, y - 1}),
         do: [:north | moves],
         else: moves

    moves =
      if !Enum.member?(elves, {x, y + 1}) and !Enum.member?(elves, {x + 1, y + 1}) and
           !Enum.member?(elves, {x - 1, y + 1}),
         do: [:south | moves],
         else: moves

    moves =
      if !Enum.member?(elves, {x - 1, y}) and !Enum.member?(elves, {x - 1, y + 1}) and
           !Enum.member?(elves, {x - 1, y - 1}),
         do: [:west | moves],
         else: moves

    moves =
      if !Enum.member?(elves, {x + 1, y}) and !Enum.member?(elves, {x + 1, y + 1}) and
           !Enum.member?(elves, {x + 1, y - 1}),
         do: [:east | moves],
         else: moves

    moves
  end

  defp proposal(elve, possible_moves, round) do
    Enum.reduce_while(0..(length(@proposals) - 1), nil, fn i, _ ->
      proposal = Enum.at(@proposals, rem(round + i, length(@proposals)))

      case proposal in possible_moves do
        true ->
          {:halt, {:ok, move_elve(elve, proposal)}}

        false ->
          {:cont, {:no, nil}}
      end
    end)
  end

  defp move_elve({x, y}, :north), do: {x, y - 1}
  defp move_elve({x, y}, :south), do: {x, y + 1}
  defp move_elve({x, y}, :west), do: {x - 1, y}
  defp move_elve({x, y}, :east), do: {x + 1, y}

  defp parse(elves) do
    Enum.reduce(elves, {[], 0}, fn row, {elves, i} ->
      {Enum.reduce(row, {elves, 0}, fn elve, {elves, j} ->
         case elve do
           "#" -> {[{j, i} | elves], j + 1}
           _ -> {elves, j + 1}
         end
       end)
       |> elem(0), i + 1}
    end)
    |> elem(0)
    |> Enum.reverse()
  end
end
