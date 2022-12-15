defmodule AoC22.Day15.BTest do
  use ExUnit.Case

  alias AoC22.Day15.B

  test "solve" do
    assert B.solve("input/15_test_1.txt") == 56000011
  end
end
