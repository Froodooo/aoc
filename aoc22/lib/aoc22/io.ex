defmodule AoC22.Io do
  @cookie Application.compile_env!(:aoc22, :cookie)

  @spec input(non_neg_integer(), non_neg_integer()) :: binary
  def input(year, day, input \\ nil)

  def input(_year, _day, input) when input != nil do
    input
    |> File.read!()
  end

  def input(year, day, _test) do
    "https://adventofcode.com/#{year}/day/#{day}/input"
    |> HTTPoison.get!(cookie: @cookie)
    |> Map.get(:body)
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
