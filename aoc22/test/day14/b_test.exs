defmodule AoC22.Day14.BTest do
  use ExUnit.Case

  alias AoC22.Day14.B

  test "solve" do
    assert B.solve("input/14_test_1.txt") == 93
  end
end
