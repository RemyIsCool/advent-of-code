lines =
  File.read!("input.txt")
  |> String.split("\n")

trees =
  Enum.with_index(lines)
  |> Enum.reduce([], fn {line, y}, acc ->
    String.graphemes(line)
    |> Enum.with_index()
    |> Enum.reduce(acc, fn {char, x}, acc ->
      case char do
        "." -> acc
        "#" -> [{x, y} | acc]
      end
    end)
  end)

is_tree = &Enum.any?(trees, fn tree -> tree == &1 end)

slope = fn {r, d} ->
  Enum.count(
    0..Enum.count(lines),
    &is_tree.({rem(&1 * r, Enum.at(lines, 0) |> String.length()), &1 * d})
  )
end

Enum.product_by([{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}], slope) |> IO.inspect()
