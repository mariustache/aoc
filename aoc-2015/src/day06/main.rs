use std::env;
use std::fs;
use regex::Regex;

use utils::solution;

const DIMENSION: usize = 1000;

type LightsGrid = [[i32; DIMENSION]; DIMENSION];

#[derive(Debug)]
enum CommandType {
    TURNON = 0,
    TURNOFF,
    TOGGLE,
    INVALID
}

#[derive(Debug)]
struct Command {
    command: CommandType,
    start_x: usize,
    start_y: usize,
    stop_x: usize,
    stop_y: usize
}

fn update_lights(grid: &mut LightsGrid, commands: &Vec<Command>, part_one: bool) {
    for command in commands {
        for row in command.start_x..command.stop_x+1 {
            for col in command.start_y..command.stop_y+1 { 
                if part_one {
                    grid[row][col] = match &command.command {
                        CommandType::TURNON => true as i32,
                        CommandType::TURNOFF => false as i32,
                        CommandType::TOGGLE => (grid[row][col] == 0) as i32,
                        CommandType::INVALID => false as i32
                    };
                } else {
                    grid[row][col] += match &command.command {
                        CommandType::TURNON => 1,
                        CommandType::TURNOFF => -1,
                        CommandType::TOGGLE => 2,
                        CommandType::INVALID => 0
                    };
                    if grid[row][col] < 0 {
                        grid[row][col] = 0;
                    }
                }
            }
        }
    }
}

fn count_lights(grid: &LightsGrid) -> i32 {
    let mut lit_lights = 0;
    for (i, row) in grid.iter().enumerate() {
        for (j, _) in row.iter().enumerate() {
            if grid[i][j] == 1 {
                lit_lights += 1;
            }
        }
    }
    lit_lights
}

fn total_brightness(grid: &LightsGrid) -> i32 {
    let total: i32 = grid.iter().map(|x| -> i32 { x.iter().sum() }).sum();
    total
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
            "turn on" => CommandType::TURNON,
            "turn off" => CommandType::TURNOFF,
            "toggle" => CommandType::TOGGLE,
            _ => CommandType::INVALID
        };
        commands.push(
            Command {
                command,
                start_x: groups["start_x"].parse::<usize>().unwrap(),
                start_y: groups["start_y"].parse::<usize>().unwrap(),
                stop_x: groups["stop_x"].parse::<usize>().unwrap(),
                stop_y: groups["stop_y"].parse::<usize>().unwrap()
            }
        );
    }
    let mut grid: LightsGrid = [[0; DIMENSION]; DIMENSION];
    update_lights(&mut grid, &commands, true);
    solution!("1", count_lights(&grid));
    let mut grid: LightsGrid = [[0; DIMENSION]; DIMENSION];
    update_lights(&mut grid, &commands, false);
    solution!("2", total_brightness(&grid));
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