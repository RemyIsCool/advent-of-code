defmodule Day1 do
  def calc_fuels(fuel) do
    required = floor(fuel / 3) - 2
    if required > 0, do: required + calc_fuels(required), else: 0
  end
end

File.read!("input.txt")
|> String.split("\n")
|> Enum.map(&String.to_integer/1)
|> Enum.sum_by(&Day1.calc_fuels/1)
|> IO.inspect()
