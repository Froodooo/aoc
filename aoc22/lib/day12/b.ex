defmodule AoC22.Day12.B do
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

    {sy, sx} = Matrix.find(matrix, @start)
    {fy, fx} = finish = Matrix.find(matrix, @finish)

    matrix = put_in(matrix[sy][sx], ?a)
    matrix = put_in(matrix[fy][fx], ?z)

    queue = Matrix.find_all(matrix, ?a)

    bfs(matrix, queue, finish)
  end

  defp bfs(matrix, queue, finish, visited \\ [])

  defp bfs(_matrix, [{{y, x}, steps} | _queue], {y, x}, _visited), do: steps

  defp bfs(matrix, [{{sy, sx}, steps} | queue], finish, visited) do
    if {sy, sx} in visited do
      bfs(matrix, queue, finish, visited)
    else
      visited = [{sy, sx} | visited]

      queue =
        Enum.concat(
          queue,
          Enum.filter(
            [
              {{sy - 1, sx}, steps + 1},
              {{sy + 1, sx}, steps + 1},
              {{sy, sx - 1}, steps + 1},
              {{sy, sx + 1}, steps + 1}
            ],
            fn
              {{y, x}, _} ->
                matrix[y][x] != nil and
                  {y, x} not in visited and
                  matrix[y][x] <= matrix[sy][sx] + 1
            end
          )
        )

      bfs(matrix, queue, finish, visited)
    end
  end
end
