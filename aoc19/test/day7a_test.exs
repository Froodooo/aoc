defmodule Aoc19.Day7aTest do
  use ExUnit.Case

  alias Aoc19.Day7a

  test "it should handle actual input" do
    assert 67023 = Day7a.start("input/7")
  end

  test "it should handle example input" do
    assert 43210 = Day7a.start("input/7a_example1")
    assert 54321 = Day7a.start("input/7a_example2")
    assert 65210 = Day7a.start("input/7a_example3")
  end
end
