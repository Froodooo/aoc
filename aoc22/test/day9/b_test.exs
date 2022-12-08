defmodule AoC22.Day9.BTest do
  use ExUnit.Case

  alias AoC22.Day9.B

  test "solve" do
    assert B.solve("input/9_test_1.txt") == :result
  end
end
