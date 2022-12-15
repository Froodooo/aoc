defmodule AoC22.Day16.BTest do
  use ExUnit.Case

  alias AoC22.Day16.B

  test "solve" do
    assert B.solve("input/16_test_1.txt") == :result
  end
end
