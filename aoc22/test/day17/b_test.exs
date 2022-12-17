defmodule AoC22.Day17.BTest do
  use ExUnit.Case

  alias AoC22.Day17.B

  test "solve" do
    assert B.solve("input/17_test_1.txt") == :result
  end
end
