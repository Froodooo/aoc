defmodule Aoc19.Day3bTest do
  use ExUnit.Case

  alias Aoc19.Day3b

  test "handles real input" do
    assert 48012 = Day3b.start("input/3")
  end

  test "handles test input" do
    assert 610 = Day3b.start("input/3b_example1")
    assert 410 = Day3b.start("input/3b_example2")
  end
end
