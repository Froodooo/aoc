defmodule AoC22.Day23.ATest do
  use ExUnit.Case

  alias AoC22.Day23.A

  test "solve" do
    assert A.solve("input/23_test_1.txt") == 110
  end
end
