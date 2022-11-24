defmodule Aoc19.Day9aTest do
  use ExUnit.Case

  alias Aoc19.Day9a

  test "it should have final answer" do
    assert 4_234_906_522 = Day9a.start("input/9")
  end

  test "it should handle example input" do
    assert 99 = Day9a.start("input/9a_example1")
    assert 1_219_070_632_396_864 = Day9a.start("input/9a_example2")
    assert 1_125_899_906_842_624 = Day9a.start("input/9a_example3")
  end
end
