File.read!("input.txt")
|> String.graphemes()
|> Enum.with_index()
|> Enum.reduce_while(0, fn {paren, i}, acc ->
  new =
    case paren do
      "(" -> acc + 1
      ")" -> acc - 1
    end

  if new < 0 do
    {:halt, i + 1}
  else
    {:cont, new}
  end
end)
|> IO.inspect()
