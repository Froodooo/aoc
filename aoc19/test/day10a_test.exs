defmodule Aoc19.Day10aTest do
  use ExUnit.Case

  alias Aoc19.Day10a

  test "it should handle actual input" do
    assert 303 = Day10a.start("input/10")
  end

  test "it should handle example input" do
    assert 8 = Day10a.start("input/10a_example1")
    assert 33 = Day10a.start("input/10a_example2")
    assert 35 = Day10a.start("input/10a_example3")
    assert 41 = Day10a.start("input/10a_example4")
    assert 210 = Day10a.start("input/10a_example5")
  end
end
