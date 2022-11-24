defmodule Aoc19.Utils.Common do
  @moduledoc false

  def read(input, separator \\ "\n") do
    input
    |> File.read!()
    |> String.split(separator)
    |> Enum.filter(&(&1 != ""))
  end

  def read_lines(input) do
    input
    |> File.read!()
    |> String.split("\n")
    |> Enum.reverse()
    |> tl()
    |> Enum.reverse()
  end

  def read_numbers(input, separator \\ "\n") do
    input
    |> File.read!()
    |> String.split(separator)
    |> Enum.filter(&(&1 != ""))
    |> Enum.map(&String.to_integer(String.trim(&1)))
  end

  def read_text(input, separator \\ "\n") do
    input
    |> File.read!()
    |> String.split(separator)
    |> Enum.filter(&(&1 != ""))
    |> Enum.map(&String.trim/1)
  end
end
