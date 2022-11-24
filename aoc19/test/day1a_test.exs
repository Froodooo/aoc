defmodule Aoc19.Day1aTest do
  use ExUnit.Case

  alias Aoc19.Day1a

  test "it should have final answer" do
    assert 3_364_035 = Day1a.start("input/1")
  end
end
