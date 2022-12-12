defmodule AoC22.Day12.A do
  alias AoC22.Utils
  alias AoC22.Day12.Matrix

  @start 83
  @finish 69

  def solve(input) do
    grid =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&String.to_charlist/1)
      |> Matrix.from_list()

    start = Matrix.find(grid, @start)
    finish = Matrix.find(grid, @finish)

    Matrix.pathfind(grid, start, finish)
  end
end
