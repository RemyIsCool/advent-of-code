use itertools::Itertools;
use std::fs::read_to_string;

fn main() {
    let (left, right): (Vec<_>, Vec<_>) = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|str| str.parse::<i32>().unwrap())
                .next_tuple::<(_, _)>()
                .unwrap()
        })
        .unzip::<_, _, Vec<_>, Vec<_>>();

    let answer = left
        .into_iter()
        .map(|num| {
            num * right
                .clone()
                .into_iter()
                .filter(|&num2| num == num2)
                .count() as i32
        })
        .sum::<i32>();

    println!("{}", answer);
}
