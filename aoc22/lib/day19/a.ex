defmodule AoC22.Day19.A do
  alias AoC22.Utils

  def solve(input) do
    blueprints =
      input
      |> Utils.input()
      |> String.split("\n")
      |> Enum.map(&parse_blueprints/1)

    Enum.reduce(blueprints, 0, fn %{id: id} = blueprint, acc ->
      robots = init_robots()
      materials = init_materials()
      maxes = init_maxes(blueprint)
      geodes = run_blueprint(blueprint, robots, materials, maxes, 1)
      acc + geodes * id
    end)

    :result
  end

  defp init_maxes(blueprint) do
    %{
      ore:
        Enum.max([
          blueprint.ore_robot_ore_costs,
          blueprint.clay_robot_ore_costs,
          blueprint.obsidian_robot_ore_costs,
          blueprint.geode_robot_ore_costs
        ]),
      clay: blueprint.obsidian_robot_clay_costs,
      obsidian: blueprint.geode_robot_obsidian_costs
    }
  end

  defp run_blueprint(_blueprint, _robots, %{geode: geode}, _maxes, 24), do: geode

  defp run_blueprint(blueprint, robots, materials, maxes, minutes) do
    # IO.inspect(minutes, label: "minutes")

    {updated_robots, updated_materials} =
      {robots, materials}
      |> buy_geode_robot(blueprint, materials)
      |> buy_obsidian_robot(blueprint, materials, maxes)
      |> buy_clay_robot(blueprint, materials, maxes)
      |> buy_ore_robot(blueprint, materials, maxes)

    # IO.inspect(updated_robots, label: "robots")
    # IO.inspect(updated_materials, label: "materials")

    # |> IO.inspect(label: "mined materials")
    mined_materials = mine_materials(updated_materials, robots)

    run_blueprint(blueprint, updated_robots, mined_materials, maxes, minutes + 1)
  end

  defp mine_materials(materials, robots) do
    materials
    |> Map.update(:geode, 0, &(&1 + Map.get(robots, :geode, 0)))
    |> Map.update(:obsidian, 0, &(&1 + Map.get(robots, :obsidian, 0)))
    |> Map.update(:clay, 0, &(&1 + Map.get(robots, :clay, 0)))
    |> Map.update(:ore, 0, &(&1 + Map.get(robots, :ore, 0)))
  end

  defp buy_geode_robot(
         {robots, materials},
         %{geode_robot_ore_costs: ore_costs, geode_robot_obsidian_costs: obsidian_costs},
         %{ore: ore, obsidian: obsidian}
       )
       when ore >= ore_costs and obsidian >= obsidian_costs do
    updated_robots = Map.update(robots, :geode, 1, &(&1 + 1))

    updated_materials =
      materials
      |> Map.update(:obsidian, 0, &(&1 - obsidian_costs))
      |> Map.update(:ore, 0, &(&1 - ore_costs))

    {updated_robots, updated_materials}
  end

  defp buy_geode_robot({robots, materials}, _blueprint, _materials), do: {robots, materials}

  defp buy_obsidian_robot(
         {%{obsidian: obsidian_robots} = robots, materials},
         %{obsidian_robot_ore_costs: ore_costs, obsidian_robot_clay_costs: clay_costs},
         %{ore: ore, clay: clay},
         %{obsidian: obsidian_max}
       )
       when ore >= ore_costs and clay >= clay_costs and obsidian_robots <= obsidian_max do
    updated_robots = Map.update(robots, :obsidian, 1, &(&1 + 1))

    updated_materials =
      materials
      |> Map.update(:clay, 0, &(&1 - clay_costs))
      |> Map.update(:ore, 0, &(&1 - ore_costs))

    {updated_robots, updated_materials}
  end

  defp buy_obsidian_robot({robots, materials}, _blueprint, _materials, _maxes),
    do: {robots, materials}

  defp buy_clay_robot(
         {%{clay: clay_robots} = robots, materials},
         %{clay_robot_ore_costs: ore_costs},
         %{ore: ore},
         %{clay: clay_max}
       )
       when ore >= ore_costs and clay_robots <= clay_max do
    updated_robots = Map.update(robots, :clay, 1, &(&1 + 1))
    updated_materials = materials |> Map.update(:ore, 0, &(&1 - ore_costs))
    {updated_robots, updated_materials}
  end

  defp buy_clay_robot({robots, materials}, _blueprint, _materials, _maxes),
    do: {robots, materials}

  defp buy_ore_robot(
         {%{ore: ore_robots} = robots, materials},
         %{ore_robot_ore_costs: ore_costs},
         %{ore: ore},
         %{ore: ore_max}
       )
       when ore >= ore_costs and ore_robots <= ore_max do
    updated_robots = Map.update(robots, :ore, 1, &(&1 + 1))
    updated_materials = materials |> Map.update(:ore, 0, &(&1 - ore_costs))
    {updated_robots, updated_materials}
  end

  defp buy_ore_robot({robots, materials}, _blueprint, _materials, _maxes), do: {robots, materials}

  defp parse_blueprints(blueprint) do
    ~r/Blueprint (?<id>\d+): Each ore robot costs (?<ore_robot_ore_costs>\d+) ore. Each clay robot costs (?<clay_robot_ore_costs>\d+) ore. Each obsidian robot costs (?<obsidian_robot_ore_costs>\d+) ore and (?<obsidian_robot_clay_costs>\d+) clay. Each geode robot costs (?<geode_robot_ore_costs>\d+) ore and (?<geode_robot_obsidian_costs>\d+) obsidian./
    |> Regex.named_captures(blueprint)
    |> Map.new(fn {k, v} -> {String.to_atom(k), String.to_integer(v)} end)
  end

  defp init_robots() do
    %{
      ore: 1,
      clay: 0,
      obsidian: 0,
      geode: 0
    }
  end

  defp init_materials() do
    %{
      ore: 0,
      clay: 0,
      obsidian: 0,
      geode: 0
    }
  end
end
