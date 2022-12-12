defmodule AoC22.Day12.A do
  alias AoC22.Utils
  alias AoC22.Day12.Matrix

  @start 83
  @finish 69

  def solve(input) do
    matrix =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&String.to_charlist/1)
      |> Matrix.from_list()

    {sy, sx} = start = Matrix.find(matrix, @start)
    {fy, fx} = finish = Matrix.find(matrix, @finish)

    matrix = put_in(matrix[sy][sx], ?a)
    matrix = put_in(matrix[fy][fx], ?z)

    Matrix.pathfind(matrix, start, finish)
  end
end
