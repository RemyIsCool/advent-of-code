input =
  File.read!("input.txt")
  |> String.split("\n")
  |> Enum.map(fn line ->
    [range, letter, password] = String.split(line)
    letter = String.at(letter, 0)
    counts = String.split(range, "-") |> Enum.map(&elem(Integer.parse(&1), 0))
    {counts, letter, password}
  end)

Enum.count(input, fn {[first, second], letter, password} ->
  at_first = String.at(password, first - 1) == letter
  at_second = String.at(password, second - 1) == letter
  (at_first or at_second) and not (at_first and at_second)
end)
|> IO.inspect()

Enum.count(input, fn {[min_count, max_count], letter, password} ->
  count = String.graphemes(password) |> Enum.count(fn char -> char == letter end)
  count >= min_count and count <= max_count
end)

# |> IO.inspect()
