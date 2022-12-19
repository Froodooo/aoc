defmodule AoC22.Day19.BTest do
  use ExUnit.Case

  alias AoC22.Day19.B

  test "solve" do
    assert B.solve("input/19_test_1.txt") == :result
  end
end
