require Integer

calc_santa = fn moves ->
  Enum.map_reduce(moves, {0, 0}, fn {movement, _}, {x, y} ->
    new_pos =
      case movement do
        ">" -> {x + 1, y}
        "v" -> {x, y + 1}
        "<" -> {x - 1, y}
        "^" -> {x, y - 1}
      end

    {new_pos, new_pos}
  end)
end

instructions =
  File.read!("input.txt")
  |> String.graphemes()

{santa, robot} =
  Enum.with_index(instructions)
  |> Enum.split_with(fn {_, i} -> Integer.is_even(i) end)

{santa, _} = calc_santa.(santa)
{robot, _} = calc_santa.(robot)

Enum.uniq([{0, 0} | santa ++ robot]) |> Enum.count() |> IO.inspect()
