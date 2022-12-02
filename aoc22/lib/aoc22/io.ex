defmodule AoC22.Io do
  @cookie Application.compile_env!(:aoc22, :cookie)

  @spec input(non_neg_integer() | binary) :: binary
  def input(day) when is_number(day) do
    "https://adventofcode.com/2022/day/#{day}/input"
    |> HTTPoison.get!(cookie: @cookie)
    |> Map.get(:body)
  end

  def input(input) when is_binary(input) do
    input
    |> File.read!()
    |> String.trim()
  end
end
