grid =
  File.read!("input.txt")
  |> String.split("\n")
  |> Enum.map(fn line ->
    String.graphemes(line)
    |> Enum.map(fn char ->
      {num, _} = Integer.parse(char)
      num
    end)
  end)

width = Enum.count(Enum.at(grid, 0))
height = Enum.count(grid)

indexed =
  grid
  |> List.flatten()
  |> Enum.with_index()
  |> Enum.map(fn {t, i} -> {t, rem(i, width), floor(i / width)} end)

Enum.map(indexed, fn {t, x, y} ->
  if x == 0 or x == width - 1 or y == 0 or y == height - 1 do
    0
  else
    right = Enum.at(grid, y) |> Enum.slice((x + 1)..-1//1)
    left = Enum.at(grid, y) |> Enum.slice(0..(x - 1)) |> Enum.reverse()
    top = Enum.slice(grid, 0..(y - 1)) |> Enum.map(&Enum.at(&1, x)) |> Enum.reverse()
    bottom = Enum.slice(grid, (y + 1)..-1//1) |> Enum.map(&Enum.at(&1, x))

    Enum.product_by(
      [right, left, top, bottom],
      &Enum.reduce_while(&1, 0, fn neighbor, acc ->
        if neighbor < t do
          {:cont, acc + 1}
        else
          {:halt, acc + 1}
        end
      end)
    )
  end
end)
|> Enum.max()
|> IO.inspect()

# indexed
# |> Enum.count(fn {t, x, y} ->
#   if x == 0 or x == width - 1 or y == 0 or y == height - 1 do
#     true
#   else
#     matches = &Enum.all?(&1, fn o -> o < t end)

#     Enum.at(grid, y) |> Enum.slice((x + 1)..-1//1) |> matches.() or
#       Enum.at(grid, y) |> Enum.slice(0..(x - 1)) |> matches.() or
#       Enum.slice(grid, 0..(y - 1)) |> Enum.map(&Enum.at(&1, x)) |> matches.() or
#       Enum.slice(grid, (y + 1)..-1//1) |> Enum.map(&Enum.at(&1, x)) |> matches.()
#   end
# end)
# |> IO.inspect()
