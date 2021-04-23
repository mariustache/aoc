use std::env;
use std::fs;

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
    let mut current_char = string.chars().nth(0).expect("Empty string.");
    for _char in string.chars().skip(1) {
        if current_char == _char {
            return String::from("nice")
        }
        else {
            current_char = _char;
        }
    }
    String::from("naughty")
}

fn vowel_check(string: &String) -> String {
    let vowels: String = String::from("aeiou");
    let mut vowels_number = 3;
    for _char in string.chars() {
        if vowels.contains(_char) {
            vowels_number -= 1;
        }
    }
    if vowels_number > 0 {
        return String::from("naughty")
    }
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

#[test]
fn test_vowels() {
    let mut value = String::from("aaa");
    assert_eq!(vowel_check(&value), "nice");
    value = String::from("aab");
    assert_eq!(vowel_check(&value), "naughty");
}

#[test]
fn test_appearence() {
    let mut value = String::from("jchzalrnumimnmhp");
    assert_eq!(appearence_check(&value), "naughty");
    value = String::from("jchzalrnumimnmhpp");
    assert_eq!(appearence_check(&value), "nice");

}

#[test]
fn test_pair() {
    let mut value = String::from("haegwjzuvuyypxyu");
    assert_eq!(pair_check(&value), "naughty");
    value = String::from("haegwjzuvuyypxxu");
    assert_eq!(pair_check(&value), "nice");

}