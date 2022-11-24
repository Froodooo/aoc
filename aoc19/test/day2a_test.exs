defmodule Aoc19.Day2aTest do
  use ExUnit.Case

  alias Aoc19.Day2a

  test "it should have final answer" do
    assert 3_790_689 = Day2a.start("input/2")
  end
end
