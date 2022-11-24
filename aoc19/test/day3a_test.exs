defmodule Aoc19.Day3aTest do
  use ExUnit.Case

  alias Aoc19.Day3a

  test "handles real input" do
    assert 1431 = Day3a.start("input/3")
  end

  test "handles test input" do
    assert 159 = Day3a.start("input/3a_example1")
    assert 135 = Day3a.start("input/3a_example2")
  end
end
