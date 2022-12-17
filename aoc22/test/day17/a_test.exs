defmodule AoC22.Day17.ATest do
  use ExUnit.Case

  alias AoC22.Day17.A

  test "solve" do
    assert A.solve("input/17_test_1.txt") == 3068
  end
end
