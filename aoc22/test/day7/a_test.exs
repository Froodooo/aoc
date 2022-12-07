defmodule AoC22.Day7.ATest do
  use ExUnit.Case

  alias AoC22.Day7.A

  test "solve" do
    assert A.solve("input/7_test_1.txt") == 95437
  end
end
