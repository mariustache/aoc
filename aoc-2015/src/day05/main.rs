use std::env;
use std::fs;
use regex::Regex;

use utils::solution;

fn pair_check(string: &String) -> String {
    let pairs: Vec<&str> = vec!["ab", "cd", "pq", "xy"];
    for pair in pairs {
        if string.contains(pair) {
            println!("String {} contains {}.", string, pair);
            return String::from("naughty")
        }
    }

    return String::from("nice")
}

fn appearence_check(string: &String) -> String {
    let re = Regex::new(r"([a-z])\1").unwrap();
    if re.is_match(string) {
        return String::from("nice")
    }
    String::from("naughty")
}

fn vowel_check(string: &String) -> String {

    String::from("nice")
}

fn string_type(string: &String) -> String {
    let check_functions: Vec<fn(&String) -> String> = vec![pair_check, appearence_check, vowel_check];
    for check_function in check_functions {
        if check_function(&string) == "naughty" {
            return String::from("naughty")
        }
    }

    String::from("nice")
}

fn solve(data: &String) {
    let data: String = fs::read_to_string(&data).
        expect("Error reading input file!");
    let mut nice_strings = 0;
    for string in data.split("\n") {
        if string_type(&string.to_string()) == "nice" {
            nice_strings += 1;
        }
    }
    solution!("1", nice_strings);

    //let solution: u32 = find_hash(&secret_key, NONCE6);
    //solution!("2", solution);
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        1 => println!("Please provide input file."),
        2 => solve(&args[1]),
        _ => println!("Too many arguments!"),
    }
}