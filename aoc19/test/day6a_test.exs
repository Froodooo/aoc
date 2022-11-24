defmodule Aoc19.Day6aTest do
  use ExUnit.Case

  alias Aoc19.Day6a

  test "it handles actual input" do
    314_247 = Day6a.start("input/6")
  end

  test "it handles example input" do
    assert 42 = Day6a.start("input/6a_example1")
  end
end
