defmodule Aoc19.Day12bTest do
  use ExUnit.Case

  alias Aoc19.Day12b

  test "it handles actual input" do
    467034091553512 = Day12b.start("input/12")
  end

  test "it handles example input" do
    2772 = Day12b.start("input/12a_example1")
    4686774924 = Day12b.start("input/12a_example2")
  end
end
