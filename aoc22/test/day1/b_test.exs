defmodule BTest do
  use ExUnit.Case

  alias AoC22.Day1.B

  test "solve" do
    assert B.solve("input/1_test_1.txt") == 45000
  end
end
