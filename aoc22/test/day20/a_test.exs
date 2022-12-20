defmodule AoC22.Day20.ATest do
  use ExUnit.Case

  alias AoC22.Day20.A

  test "solve" do
    assert A.solve("input/20_test_1.txt") == 3
  end
end
