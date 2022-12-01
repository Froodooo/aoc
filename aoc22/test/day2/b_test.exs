defmodule AoC22.Day2.BTest do
  use ExUnit.Case

  alias AoC22.Day2.B

  test "solve" do
    assert B.solve("input/1_test_1.txt") == :result
  end
end
