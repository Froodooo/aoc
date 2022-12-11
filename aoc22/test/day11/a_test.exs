defmodule AoC22.Day11.ATest do
  use ExUnit.Case

  alias AoC22.Day11.A

  test "solve" do
    assert A.solve("input/11_test_1.txt") == 10605
  end
end
