defmodule AoC22.Day2.ATest do
  use ExUnit.Case

  alias AoC22.Day2.A

  test "solve" do
    assert A.solve("input/2_test_1.txt") == 15
  end
end
