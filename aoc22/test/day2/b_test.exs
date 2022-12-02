defmodule AoC22.Day2.BTest do
  use ExUnit.Case

  alias AoC22.Day2.B

  test "solve" do
    assert B.solve("input/2_test_1.txt") == 12
  end
end
