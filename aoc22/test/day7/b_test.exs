defmodule AoC22.Day7.BTest do
  use ExUnit.Case

  alias AoC22.Day7.B

  test "solve" do
    assert B.solve("input/7_test_1.txt") == 24_933_642
  end
end
