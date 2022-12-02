defmodule AoC22.Day2.B do
  alias AoC22.Io

  @rock 1
  @paper 2
  @scissors 3

  @lose 0
  @draw 3
  @win 6

  def solve(input) do
    input
    |> Io.input()
    |> String.split("\n")
    |> Enum.map(&String.split/1)
    |> Enum.reduce(0, &score/2)
  end

  defp score([], total), do: total
  defp score(["A", "X"], total), do: total + @scissors + @lose
  defp score(["A", "Y"], total), do: total + @rock + @draw
  defp score(["A", "Z"], total), do: total + @paper + @win
  defp score(["B", "X"], total), do: total + @rock + @lose
  defp score(["B", "Y"], total), do: total + @paper + @draw
  defp score(["B", "Z"], total), do: total + @scissors + @win
  defp score(["C", "X"], total), do: total + @paper + @lose
  defp score(["C", "Y"], total), do: total + @scissors + @draw
  defp score(["C", "Z"], total), do: total + @rock + @win
end
