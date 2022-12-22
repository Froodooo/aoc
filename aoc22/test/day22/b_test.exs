defmodule AoC22.Day22.BTest do
  use ExUnit.Case

  alias AoC22.Day22.B

  test "solve" do
    assert B.solve("input/22_test_1.txt") == :result
  end
end
