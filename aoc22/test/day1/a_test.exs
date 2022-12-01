defmodule ATest do
  use ExUnit.Case

  alias AoC22.Day1.A

  test "solve" do
    assert A.solve(2022, 1, "input/1_test_1.txt") == 24000
  end
end
