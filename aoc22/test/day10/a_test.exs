defmodule AoC22.Day10.ATest do
  use ExUnit.Case

  alias AoC22.Day10.A

  test "solve" do
    assert A.solve("input/10_test_1.txt") == 13140
  end
end
