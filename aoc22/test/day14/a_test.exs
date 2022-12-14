defmodule AoC22.Day14.ATest do
  use ExUnit.Case

  alias AoC22.Day14.A

  test "solve" do
    assert A.solve("input/14_test_1.txt") == 24
  end
end
