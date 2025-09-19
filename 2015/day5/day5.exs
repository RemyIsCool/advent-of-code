File.read!("input.txt")
|> String.split()
|> Enum.count(fn string ->
  chars = String.graphemes(string)

  chunks =
    Enum.chunk_every(chars, 2, 1, :discard)
    |> Enum.with_index()

  chunks
  |> Enum.any?(fn {part, i} ->
    Enum.any?(chunks, fn {part2, i2} ->
      part2 == part and (i2 < i - 1 or i2 > i + 1)
    end)
  end)
  |> IO.inspect(label: "pair") and
    Enum.chunk_every(chars, 3, 1, :discard)
    |> Enum.any?(fn [a, _, c] -> a == c end)
    |> IO.inspect(label: "once between")

  # Enum.count(chars, &(&1 in ~w(a e i o u))) >= 3 and
  #   Enum.chunk_every(chars, 2, 1, :discard)
  #   |> Enum.any?(fn [a, b] -> a == b end) and
  #   Enum.all?(~w(ab cd pq xy), &(not String.contains?(string, &1)))
end)
|> IO.inspect()
