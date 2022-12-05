defmodule AoC22.Utils do
  @cookie Application.compile_env!(:aoc22, :cookie)

  @spec input(non_neg_integer() | binary) :: binary
  def input(day, opts \\ %{trim: true})

  def input(day, opts) when is_number(day) do
    "https://adventofcode.com/2022/day/#{day}/input"
    |> HTTPoison.get!(cookie: @cookie)
    |> Map.get(:body)
    |> input_opts(opts)
  end

  def input(input, opts) when is_binary(input) do
    input
    |> File.read!()
    |> input_opts(opts)
  end

  def input_opts(input, %{trim: true}), do: String.trim(input)
  def input_opts(input, _opts), do: input
end
