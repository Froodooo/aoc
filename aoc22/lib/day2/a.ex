defmodule AoC22.Day2.A do
  alias AoC22.Utils

  @rock 1
  @paper 2
  @scissors 3

  @lose 0
  @draw 3
  @win 6

  def solve(input) do
    input
    |> Utils.input()
    |> String.split("\n")
    |> Enum.map(&String.split/1)
    |> Enum.reduce(0, &score/2)
  end

  defp score([], total), do: total
  defp score(["A", "X"], total), do: total + @rock + @draw
  defp score(["A", "Y"], total), do: total + @paper + @win
  defp score(["A", "Z"], total), do: total + @scissors + @lose
  defp score(["B", "X"], total), do: total + @rock + @lose
  defp score(["B", "Y"], total), do: total + @paper + @draw
  defp score(["B", "Z"], total), do: total + @scissors + @win
  defp score(["C", "X"], total), do: total + @rock + @win
  defp score(["C", "Y"], total), do: total + @paper + @lose
  defp score(["C", "Z"], total), do: total + @scissors + @draw
end
