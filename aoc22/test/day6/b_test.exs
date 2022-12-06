defmodule AoC22.Day6.BTest do
  use ExUnit.Case

  alias AoC22.Day6.B

  test "solve example 1" do
    assert B.solve("input/6_test_1.txt") == 19
  end
end
