defmodule Day5 do
  def search(_halves, low, high, _lower, _upper) when low == high, do: low

  def search(halves, low, high, lower, upper) do
    [half | rest] = halves
    midpoint = floor(low + (high - low) / 2)

    case half do
      ^lower -> search(rest, low, midpoint, lower, upper)
      ^upper -> search(rest, midpoint + 1, high, lower, upper)
    end
  end
end

lines =
  File.read!("input.txt")
  |> String.split()

seats =
  Enum.map(lines, fn line ->
    {row_halves, col_halves} = String.split_at(line, 7)
    row = Day5.search(String.graphemes(row_halves), 0, 127, "F", "B")
    col = Day5.search(String.graphemes(col_halves), 0, 7, "L", "R")
    row * 8 + col
  end)
  |> Enum.sort()

Enum.max(seats) |> IO.inspect()

for {seat_a, seat_b} <- Enum.zip(seats, Enum.slice(seats, 1..-1//1)) do
  if seat_a + 1 != seat_b do
    IO.inspect(seat_a + 1)
  end
end
