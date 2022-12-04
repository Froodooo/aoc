defmodule AoC22.Day4.BTest do
  use ExUnit.Case

  alias AoC22.Day4.B

  test "solve" do
    assert B.solve("input/4_test_1.txt") == 4
  end
end
