defmodule Aoc19.Day1bTest do
  use ExUnit.Case

  alias Aoc19.Day1b

  test "it should have final answer" do
    assert 5_043_167 = Day1b.start("input/1")
  end
end
