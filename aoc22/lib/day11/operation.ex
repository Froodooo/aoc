defmodule AoC22.Day11.Operation do
  def execute(item, {"*", "old"}), do: item * item
  def execute(item, {"+", "old"}), do: item + item
  def execute(item, {"*", term}), do: item * term
  def execute(item, {"+", term}), do: item + term
end
