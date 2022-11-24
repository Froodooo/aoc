defmodule Aoc19.Day7bTest do
  use ExUnit.Case

  alias Aoc19.Day7b

  test "it should handle actual input" do
    assert 7_818_398 = Day7b.start("input/7")
  end

  test "it should handle example input" do
    assert 139_629_729 = Day7b.start("input/7b_example1")
    assert 18216 = Day7b.start("input/7b_example2")
  end
end
