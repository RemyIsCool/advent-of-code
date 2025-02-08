File.read!("input.txt")
|> String.split("\n\n")
|> Enum.map(fn elf ->
  String.split(elf, "\n")
  |> Enum.map(fn food ->
    {cals, _} = Integer.parse(food)
    cals
  end)
  |> Enum.sum()
end)
|> Enum.sort()
|> Enum.slice(-3..-1//1)
|> Enum.sum()
|> IO.inspect()
