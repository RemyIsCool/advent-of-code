nums = File.read!("input.txt") |> String.split("\n") |> Enum.map(&String.to_integer/1)

for num_a <- nums do
  for num_b <- nums do
    for num_c <- nums do
      if num_a + num_b + num_c == 2020 do
        num_a * num_b * num_c
      end
    end
  end
end
|> List.flatten()
|> Enum.filter(&(&1 != nil))
|> Enum.at(0)
|> IO.inspect()
