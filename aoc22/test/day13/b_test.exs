defmodule AoC22.Day13.BTest do
  use ExUnit.Case

  alias AoC22.Day13.B

  test "solve" do
    assert B.solve("input/13_test_1.txt") == :result
  end
end
