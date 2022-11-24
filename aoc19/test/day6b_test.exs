defmodule Aoc19.Day6bTest do
  use ExUnit.Case

  alias Aoc19.Day6b

  test "it handles actual input" do
    514 = Day6b.start("input/6")
  end

  test "it handles example input" do
    assert 4 = Day6b.start("input/6b_example1")
  end
end
