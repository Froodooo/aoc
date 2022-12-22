defmodule AoC22.Day22.ATest do
  use ExUnit.Case

  alias AoC22.Day22.A

  test "solve" do
    assert A.solve("input/22_test_1.txt") == 6032
  end
end
