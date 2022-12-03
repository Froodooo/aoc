defmodule AoC22.Day3.ATest do
  use ExUnit.Case

  alias AoC22.Day3.A

  test "solve" do
    assert A.solve("input/3_test_1.txt") == 157
  end
end
