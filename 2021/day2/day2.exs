File.read("input.txt")
|> elem(1)
|> String.trim()
|> String.split("\n")
|> Enum.map(fn line ->
  [dir, len] = String.split(line)
  {len, _} = Integer.parse(len)
  {dir, len}
end)
|> Enum.reduce([0, 0, 0], fn {dir, len}, [x, y, a] ->
  case dir do
    "down" -> [x, y, a + len]
    "up" -> [x, y, a - len]
    "forward" -> [x + len, y + a * len, a]
  end
end)
|> Enum.take(2)
|> Enum.product()
|> IO.puts()
