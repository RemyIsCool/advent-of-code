windows =
  File.read!("input.txt")
  |> String.split("\n")
  |> Enum.map(&String.to_integer/1)
  |> Enum.chunk_every(3, 1)
  |> Enum.map(&Enum.sum/1)

Enum.zip(windows, Enum.slice(windows, 1..-1//1))
|> Enum.count(fn {a, b} -> a < b end)
|> IO.inspect()
