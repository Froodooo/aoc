defmodule AoC22.Day21.ATest do
  use ExUnit.Case

  alias AoC22.Day21.A

  test "solve" do
    assert A.solve("input/21_test_1.txt") == 152
  end
end
