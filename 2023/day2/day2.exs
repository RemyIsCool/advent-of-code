File.read!("input.txt")
|> String.split("\n")
|> Enum.sum_by(fn line ->
  [_, game] = String.split(line, ": ")

  game =
    game
    |> String.split("; ")
    |> Enum.map(fn part ->
      String.split(part, ", ")
      |> Enum.map(fn move ->
        [amount, color] = String.split(move)
        {String.to_integer(amount), color}
      end)
    end)

  games =
    Enum.map(game, &Map.new(&1, fn {a, b} -> {b, a} end))

  Enum.product_by(~w"red green blue", fn clr ->
    Enum.map(games, &Map.get(&1, clr, 0))
    |> Enum.max()
  end)
end)
|> IO.inspect()
