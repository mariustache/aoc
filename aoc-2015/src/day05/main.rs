use std::env;
use std::fs;

use utils::solution;

type FunctionVector = Vec<fn(&String) -> String>;

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

fn string_type(string: &String, functions: &FunctionVector) -> String {
    for check_function in functions {
        if check_function(&string) == "naughty" {
            return String::from("naughty")
        }
    }

    String::from("nice")
}

fn pair_check2(string: &String) -> String {
    let mut pair: &str = &string[..2];
    let mut index = 1;
    let max_index = (string.chars().count() - 1) - 1;
    while index != max_index {
        if string[index+1..].contains(pair) {
            return String::from("nice")
        } else {
            pair = &string[index..index+2];
            index += 1;
        }
    }
    String::from("naughty")
}

fn appearence_check2(string: &String) -> String {
    let mut letter: &str = &string[..1];
    let mut index = 1;
    let max_index = string.chars().count() - 1;
    while index != max_index {
        if letter == &string[index+1..index+2] {
            return String::from("nice")
        } else {
            letter = &string[index..index+1];
            index += 1;
        }
    }

    String::from("naughty")
}

fn solve(data: &String) {
    let data: String = fs::read_to_string(&data).
        expect("Error reading input file!");
    let mut nice_strings_1 = 0;
    let mut nice_strings_2 = 0;
    let check_functions_1: FunctionVector = vec![pair_check, appearence_check, vowel_check];
    let check_functions_2: FunctionVector = vec![pair_check2, appearence_check2];
    for string in data.split("\n") {
        if string_type(&string.to_string(), &check_functions_1) == "nice" {
            nice_strings_1 += 1;
        }
        if string_type(&string.to_string(), &check_functions_2) == "nice" {
            nice_strings_2 += 1;
        }
    }
    solution!("1", nice_strings_1);
    solution!("2", nice_strings_2);
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

#[test]
fn test_part2() {
    let mut value = String::from("qjhvhtzxzqqjkmpb");
    assert_eq!(pair_check2(&value), "nice");
    assert_eq!(appearence_check2(&value), "nice");
    //*
    value = String::from("xxyxx");
    assert_eq!(pair_check2(&value), "nice");
    assert_eq!(appearence_check2(&value), "nice");
    //*/
    //*
    value = String::from("uurcxstgmygtbstg");
    assert_eq!(pair_check2(&value), "nice");
    assert_eq!(appearence_check2(&value), "naughty");
    //*/
    //*
    value = String::from("ieodomkazucvgmuy");
    assert_eq!(pair_check2(&value), "naughty");
    assert_eq!(appearence_check2(&value), "nice");
    //*/
}
