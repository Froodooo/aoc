defmodule AoC22.Io do
  @cookie Application.compile_env!(:aoc22, :cookie)

  @spec input(non_neg_integer() | binary) :: binary
  def input(day) when is_number(day) do
    "https://adventofcode.com/2022/day/#{day}/input"
    |> HTTPoison.get!(cookie: @cookie)
    |> Map.get(:body)
  end

  def input(input) when is_binary(input) do
    File.read!(input)
  end

  @spec to_list(binary) :: [binary]
  def to_list(text, pattern \\ "\n") do
    text
    |> String.trim()
    |> String.split(pattern)
  end

  @spec to_number(list(binary)) :: [number]
  def to_number(list) do
    Enum.map(list, &String.to_integer/1)
  end
end
