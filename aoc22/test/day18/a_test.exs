defmodule AoC22.Day18.ATest do
  use ExUnit.Case

  alias AoC22.Day18.A

  test "solve" do
    assert A.solve("input/18_test_1.txt") == 64
  end
end
