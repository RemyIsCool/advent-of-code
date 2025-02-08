passports =
  File.read!("input.txt")
  |> String.split("\n\n")
  |> Enum.map(fn line ->
    pairs = String.split(line)
    Enum.map(pairs, &String.split(&1, ":"))
  end)

Enum.count(passports, fn passport ->
  Enum.all?(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], fn key ->
    key in Enum.map(passport, fn [key, _] -> key end)
  end) and
    Enum.all?(passport, fn [key, value] ->
      range = fn min, max ->
        {num, _} = Integer.parse(value)
        num in min..max
      end

      case key do
        "byr" ->
          range.(1920, 2002)

        "iyr" ->
          range.(2010, 2020)

        "eyr" ->
          range.(2020, 2030)

        "hgt" ->
          case Integer.parse(value) do
            {height, "cm"} -> height in 150..193
            {height, "in"} -> height in 59..76
            _ -> false
          end

        "hcl" ->
          Regex.match?(~r/^#([a-f\d]{6})$/, value)

        "ecl" ->
          value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        "pid" ->
          Regex.match?(~r/^\d{9}$/, value)

        _ ->
          true
      end
    end)
end)
|> IO.inspect()
