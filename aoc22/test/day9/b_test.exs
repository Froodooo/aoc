defmodule AoC22.Day9.BTest do
  use ExUnit.Case

  alias AoC22.Day9.B

  test "solve 1" do
    assert B.solve("input/9_test_1.txt") == 1
  end

  test "solve 2" do
    assert B.solve("input/9_test_2.txt") == 36
  end
end
