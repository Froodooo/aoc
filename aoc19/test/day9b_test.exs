defmodule Aoc19.Day9bTest do
  use ExUnit.Case

  alias Aoc19.Day9b

  test "it should have final answer" do
    # Omitted for performance
    # assert 60962 = Day9b.start("input/9")
  end

  test "it should handle example input" do
    assert 99 = Day9b.start("input/9a_example1")
    assert 1_219_070_632_396_864 = Day9b.start("input/9a_example2")
    assert 1_125_899_906_842_624 = Day9b.start("input/9a_example3")
  end
end
