positions =
  File.read!("input.txt")
  |> String.split(", ")
  |> Enum.reduce([{0, 0, 0}], fn move, acc ->
    dir = String.at(move, 0)
    amt = String.slice(move, 1..-1//1) |> String.to_integer()
    [{r, x, y} | _] = acc

    move = fn r ->
      r =
        cond do
          r > 3 -> 0
          r < 0 -> 3
          true -> r
        end

      for i <- amt..1//-1 do
        case r do
          0 -> {r, x + i, y}
          1 -> {r, x, y + i}
          2 -> {r, x - i, y}
          3 -> {r, x, y - i}
        end
      end ++
        acc
    end

    case dir do
      "R" -> move.(r + 1)
      "L" -> move.(r - 1)
    end
  end)
  |> Enum.reverse()
  |> Enum.with_index()

Enum.find_value(positions, fn {{_, x, y}, i} ->
  if Enum.find(positions, fn {{_, x2, y2}, i2} ->
       x == x2 and y == y2 and i != i2
     end) do
    abs(x) + abs(y)
  end
end)
|> IO.inspect()
