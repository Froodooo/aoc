defmodule AoC22.Day3.BTest do
  use ExUnit.Case

  alias AoC22.Day3.B

  test "solve" do
    assert B.solve("input/3_test_1.txt") == 70
  end
end
