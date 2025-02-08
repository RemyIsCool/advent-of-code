File.read!("input.txt")
|> String.split("\n\n")
|> Enum.sum_by(fn group ->
  people = String.split(group) |> Enum.map(&String.graphemes/1)

  Enum.reduce(people, [], fn person, acc ->
    Enum.reduce(person, acc, fn q, acc ->
      if Enum.all?(people, fn p -> q not in acc and q in p end), do: [q | acc], else: acc
    end)
  end)
  |> Enum.count()
end)
|> IO.inspect()
