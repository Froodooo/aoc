defmodule Aoc19.Day5bTest do
  use ExUnit.Case

  alias Aoc19.Day5b

  test "it should have final answer" do
    assert 652_726 = Day5b.start("input/5")
  end
end
