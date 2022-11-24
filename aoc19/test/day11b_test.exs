defmodule Aoc19.Day11bTest do
  use ExUnit.Case

  alias Aoc19.Day11b

  test "it should handle actual input" do
    assert 249 = Day11b.start("input/11")
  end
end
