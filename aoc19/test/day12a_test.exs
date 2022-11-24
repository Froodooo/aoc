defmodule Aoc19.Day12aTest do
  use ExUnit.Case

  alias Aoc19.Day12a

  test "it handles actual input" do
    5350 = Day12a.start("input/12")
  end

  test "it handles example input" do
    179 = Day12a.start("input/12a_example1", 10)
    1940 = Day12a.start("input/12a_example2", 100)
  end
end
