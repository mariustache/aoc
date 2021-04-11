use std::env;
use std::fs;

fn determine_floor(instructions: &String) -> i32 {
    let mut floor: i32 = 0;
    for instruction in instructions.chars() {
        match instruction {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => println!("Invalid character."),
        }
    }

    return floor;
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let instructions: String = fs::read_to_string(&args[1])
        .expect("Error reading input file.");


    println!("[Part 1] answer is: {}", determine_floor(&instructions));
}
