defmodule AoC22.Day12.BTest do
  use ExUnit.Case

  alias AoC22.Day12.B

  test "solve" do
    assert B.solve("input/12_test_1.txt") == 29
  end
end
