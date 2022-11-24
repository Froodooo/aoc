defmodule AoC22.Io do
  @cookie Application.compile_env!(:aoc22, :cookie)

  @spec input(non_neg_integer(), non_neg_integer()) :: binary
  def input(year, day) do
    "https://adventofcode.com/#{year}/day/#{day}/input"
    |> HTTPoison.get!(cookie: @cookie)
    |> Map.get(:body)
  end

  @spec to_list(binary) :: [binary]
  def to_list(text) do
    text
    |> String.trim()
    |> String.split("\n")
  end

  @spec to_number(list(binary)) :: [number]
  def to_number(list) do
    Enum.map(list, &String.to_integer/1)
  end
end
