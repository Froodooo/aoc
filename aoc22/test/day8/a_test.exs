defmodule AoC22.Day8.ATest do
  use ExUnit.Case

  alias AoC22.Day8.A

  test "solve" do
    assert A.solve("input/8_test_1.txt") == 21
  end
end
