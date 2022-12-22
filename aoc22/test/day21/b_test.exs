defmodule AoC22.Day21.BTest do
  use ExUnit.Case

  alias AoC22.Day21.B

  test "solve" do
    assert B.solve("input/21_test_1.txt") == 301
  end
end
