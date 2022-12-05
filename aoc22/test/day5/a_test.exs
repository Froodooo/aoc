defmodule AoC22.Day5.ATest do
  use ExUnit.Case

  alias AoC22.Day5.A

  test "solve" do
    assert A.solve("input/5_test_1.txt") == "CMZ"
  end
end
