defmodule AoC22.Day5.BTest do
  use ExUnit.Case

  alias AoC22.Day5.B

  test "solve" do
    assert B.solve("input/5_test_1.txt") == :result
  end
end
