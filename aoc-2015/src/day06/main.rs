use std::env;
use std::fs;
use regex::Regex;

use utils::solution;

#[derive(Debug)]
enum CommandType {
    TURN_ON = 0,
    TURN_OFF,
    TOGGLE,
    INVALID
}

#[derive(Debug)]
struct Command {
    command: CommandType,
    start_x: u32,
    start_y: u32,
    stop_x: u32,
    stop_y: u32
}


fn solve(data: &String) {
    let command_re = Regex::new(
        r"(?P<command>[\w ]+) (?P<start_x>\d+),(?P<start_y>\d+) through (?P<stop_x>\d+),(?P<stop_y>\d+)"
    ).unwrap();
    let data: String = fs::read_to_string(&data).
        expect("Error reading input file!");
    let mut commands: Vec<Command> = vec![];
    for string in data.split("\n") {
        let groups = command_re.captures(&string).unwrap();
        let command = match &groups["command"] {
            "turn on" => CommandType::TURN_ON,
            "turn off" => CommandType::TURN_OFF,
            "toggle" => CommandType::TOGGLE,
            _ => CommandType::INVALID
        };
        commands.push(
            Command {
                command,
                start_x: groups["start_x"].parse::<u32>().unwrap(),
                start_y: groups["start_y"].parse::<u32>().unwrap(),
                stop_x: groups["stop_x"].parse::<u32>().unwrap(),
                stop_y: groups["stop_y"].parse::<u32>().unwrap()

            }
        );
    }
    
    solution!("1", 0);
    solution!("2", 0);
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
fn test_part1() {

}

#[test]
fn test_part2() {

}