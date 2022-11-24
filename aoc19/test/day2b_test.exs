defmodule Aoc19.Day2bTest do
  use ExUnit.Case

  alias Aoc19.Day2b

  test "it should have final answer" do
    assert 6533 = Day2b.start("input/2")
  end
end
