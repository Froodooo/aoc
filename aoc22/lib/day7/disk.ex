defmodule AoC22.Day7.Disk do
  @dir_separator "\\"

  def traverse(instructions, path \\ [], dir_sizes \\ %{})

  def traverse([], _path, dir_sizes), do: dir_sizes

  def traverse([["$", "cd", ".."] | rest], path, dir_sizes),
    do: traverse(rest, Enum.drop(path, -1), dir_sizes)

  def traverse([["$", "cd", dir] | rest], path, dir_sizes),
    do: traverse(rest, path ++ [dir], dir_sizes)

  def traverse([["$", "ls"] | rest], path, dir_sizes), do: traverse(rest, path, dir_sizes)

  def traverse([["dir", _dir] | rest], path, dir_sizes), do: traverse(rest, path, dir_sizes)

  def traverse([[size, _filename] | rest], path, dir_sizes) do
    filesize = String.to_integer(size)

    dir_sizes =
      path
      |> Enum.with_index(1)
      |> Enum.reduce(dir_sizes, fn {_, index}, dir_sizes ->
        path_part = Enum.take(path, index)
        update_dir_sizes(dir_sizes, Enum.join(path_part, @dir_separator), filesize)
      end)

    traverse(rest, path, dir_sizes)
  end

  defp update_dir_sizes(dir_sizes, path, filesize) do
    case Map.get(dir_sizes, path) do
      nil -> Map.put(dir_sizes, path, filesize)
      _ -> Map.update!(dir_sizes, path, &(&1 + filesize))
    end
  end
end
