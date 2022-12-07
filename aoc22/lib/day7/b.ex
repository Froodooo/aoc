defmodule AoC22.Day7.B do
  alias AoC22.Utils
  alias AoC22.Day7.Disk

  @root ["/"]

  @total_disk_space 70_000_000
  @required_disk_space 30_000_000

  def solve(input) do
    dir_sizes =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&String.split/1)
      |> Disk.traverse()

    required_freeup = @required_disk_space - (@total_disk_space - Map.fetch!(dir_sizes, @root))

    dir_sizes
    |> Map.values()
    |> Enum.filter(&(&1 >= required_freeup))
    |> Enum.sort()
    |> hd()
  end
end
