defmodule AoC22.DayX.BTest do
  use ExUnit.Case

  alias AoC22.DayX.B

  test "solve" do
    assert B.solve("input/x_test_1.txt") == :result
  end
end
