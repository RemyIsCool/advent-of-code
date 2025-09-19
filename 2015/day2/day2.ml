let lines =
  In_channel.with_open_bin "input.txt" In_channel.input_all
  |> String.split_on_char '\n'
in
List.fold_left
  (fun acc line ->
    let dims = String.split_on_char 'x' line in
    let nums = List.map int_of_string dims in
    match nums with
    | l :: w :: h :: _ ->
        (* let a = l * w in
        let b = l * h in
        let c = w * h in *)
        let pa = (l * 2) + (w * 2) in
        let pb = (l * 2) + (h * 2) in
        let pc = (w * 2) + (h * 2) in
        (* acc + ((a + b + c) * 2) + min a (min b c) *)
        acc + (l * w * h) + min pa (min pb pc)
    | _ -> acc)
  0 lines
|> print_int
