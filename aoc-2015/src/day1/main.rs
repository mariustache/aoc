use std::env;
use std::fs;

const USIZE_MAX: usize = std::usize::MAX - 1;

fn determine_floor(instructions: &String) -> (i32, usize) {
    let mut floor: i32 = 0;
    let mut first_index: usize = USIZE_MAX;
    for (i, instruction) in instructions.chars().enumerate() {
        match instruction {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => println!("Invalid character."),
        }
        if first_index == USIZE_MAX && floor == -1 {
            first_index = i;
        }
    }
    // Position starts from 1 (from challenge description)
    (floor, first_index + 1)
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let instructions: String = fs::read_to_string(&args[1])
        .expect("Error reading input file.");

    let (floor_number, first_index) = determine_floor(&instructions);
    println!("[Part 1] answer is: {}", floor_number);
    println!("[Part 2] answer is: {}", first_index);
}

#[test]
fn test_part1() {
    let input_expected: Vec<(String, i32)> = vec![
        (String::from("(())"), 0),
        (String::from("()()"), 0),
        (String::from("((("), 3),
        (String::from("(()(()("), 3),
        (String::from("))((((("), 3),
        (String::from("())"), -1),
        (String::from("))("), -1),
        (String::from(")))"), -3),
        (String::from(")())())"), -3)
    ];
    
    for (_input, _expected) in input_expected {
        let (_floor, _) = determine_floor(&_input);
        assert_eq!(_floor, _expected, "Floor is {} for input {}", _floor, _input);
    }
}

#[test]
fn test_part2() {
    let input_expected: Vec<(String, usize)> = vec![
        (String::from(")"), 1),
        (String::from("()())"), 5)
    ];
    
    for (_input, _expected) in input_expected {
        let (_, _position) = determine_floor(&_input);
        assert_eq!(_position, _expected, "The position is {} for input {}", _position, _input);
    }
}