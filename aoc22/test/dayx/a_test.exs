defmodule AoC22.DayX.ATest do
  use ExUnit.Case

  alias AoC22.DayX.A

  test "solve" do
    assert A.solve("input/x_test_1.txt") == :result
  end
end
