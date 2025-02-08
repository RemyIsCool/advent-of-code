lines =
  File.read!("input.txt")
  |> String.split("\n")

# Part 1
# value =
#   Enum.reduce(
#     lines,
#     List.duplicate({0, 0}, Enum.at(lines, 0) |> String.length()),
#     fn line, acc ->
#       Enum.zip(String.graphemes(line), acc)
#       |> Enum.map(fn {char, a} ->
#         case char do
#           "0" -> {elem(a, 0) + 1, elem(a, 1)}
#           "1" -> {elem(a, 0), elem(a, 1) + 1}
#         end
#       end)
#     end
#   )
#   |> Enum.reduce("", fn {zeros, ones}, acc ->
#     acc <>
#       if zeros > ones do
#         "0"
#       else
#         "1"
#       end
#   end)

# {value1, _} = Integer.parse(value, 2)

# {value2, _} =
#   value
#   |> String.replace(["1", "0"], fn char ->
#     case char do
#       "1" -> "0"
#       "0" -> "1"
#     end
#   end)
#   |> Integer.parse(2)

# IO.puts("Part 1:")
# IO.puts(value1 * value2)
# IO.puts("")

defmodule Day3 do
  def calc(lines, req) do
    chars = Enum.map(lines, &String.graphemes/1)
    len = Enum.at(chars, 0) |> Enum.count()

    {value, _} =
      Enum.reduce(0..(len - 1), chars, fn x, rows ->
        {zeros, ones} =
          Enum.reduce(rows, {0, 0}, fn row, acc ->
            case Enum.at(row, x) do
              "0" -> {elem(acc, 0) + 1, elem(acc, 1)}
              "1" -> {elem(acc, 0), elem(acc, 1) + 1}
            end
          end)

        bit = req.(zeros, ones)

        if Enum.count(rows) > 1 do
          Enum.filter(rows, fn row -> Enum.at(row, x) == bit end)
        else
          rows
        end
      end)
      |> Enum.at(0)
      |> Enum.join()
      |> Integer.parse(2)

    value
  end
end

oxygen =
  Day3.calc(lines, fn zeros, ones ->
    if zeros > ones do
      "0"
    else
      "1"
    end
  end)

co2 =
  Day3.calc(lines, fn zeros, ones ->
    if zeros > ones do
      "1"
    else
      "0"
    end
  end)

IO.puts(oxygen * co2)
