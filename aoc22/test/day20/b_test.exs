defmodule AoC22.Day20.BTest do
  use ExUnit.Case

  alias AoC22.Day20.B

  test "solve" do
    assert B.solve("input/20_test_1.txt") == 1_623_178_306
  end
end
