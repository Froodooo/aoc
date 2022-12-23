defmodule AoC22.Day23.BTest do
  use ExUnit.Case

  alias AoC22.Day23.B

  test "solve" do
    assert B.solve("input/23_test_1.txt") == 20
  end
end
