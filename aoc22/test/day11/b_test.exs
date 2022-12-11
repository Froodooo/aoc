defmodule AoC22.Day11.BTest do
  use ExUnit.Case

  alias AoC22.Day11.B

  test "solve" do
    assert B.solve("input/11_test_1.txt") == :result
  end
end
