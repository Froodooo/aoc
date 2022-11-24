defmodule Aoc19.Day5aTest do
  use ExUnit.Case

  alias Aoc19.Day5a

  test "it should have final answer" do
    assert 15_314_507 = Day5a.start("input/5")
  end
end
