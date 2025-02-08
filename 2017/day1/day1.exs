nums =
  File.read!("input.txt")
  |> String.graphemes()
  |> Enum.map(&String.to_integer/1)

v =
  Enum.with_index(nums)
  |> Enum.map(fn {n, i} ->
    {n, Enum.at(nums, floor(Enum.count(nums) / 2) + i)}
  end)
  |> Enum.sum_by(fn {a, b} -> if a == b, do: a, else: 0 end)

# idk why this works
IO.inspect(v * 2)
