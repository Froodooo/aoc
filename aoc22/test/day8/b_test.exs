defmodule AoC22.Day8.BTest do
  use ExUnit.Case

  alias AoC22.Day8.B

  test "solve" do
    assert B.solve("input/8_test_1.txt") == :result
  end
end
