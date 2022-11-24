defmodule Aoc19.Day10bTest do
  use ExUnit.Case

  alias Aoc19.Day10b

  test "it should handle actual input" do
    assert 408 = Day10b.start("input/10")
  end
end
