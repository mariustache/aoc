use std::env;
use std::fs;
use std::collections::HashMap;

macro_rules! stringify {
    ($tuple: expr) => {
        String::from(format!("{}:{}", $tuple.0, $tuple.1));
    };
}

fn update_position(_move: &char) -> (i32, i32) {
    let mut position: (i32, i32) = (0, 0);
    match _move {
        '^' => position.1 += 1,
        'v' => position.1 -= 1,
        '>' => position.0 += 1,
        '<' => position.0 -= 1,
        _ => println!("Error! Move must be ^ v > <.")
    }

    position
}

fn visited_houses(moves: &String, mut houses: HashMap<String, u32>) -> HashMap<String, u32> {
    let mut position: (i32, i32) = (0, 0);
    *houses.entry(stringify!(position)).or_insert(1) += 1;
    for _move in moves.chars() {
        let increments = update_position(&_move);
        position.0 += increments.0;
        position.1 += increments.1;
        *houses.entry(stringify!(position)).or_insert(1) += 1;
    }
    houses
}

fn split_moves(moves: &String) -> (String, String) {
    let mut santa = String::from("");
    let mut robo_santa = String::from("");
    for (i, _move) in moves.chars().enumerate() {
        match i % 2 {
            0 => santa.push(_move),
            1 => robo_santa.push(_move),
            _ => (),
        }
    }
    (santa, robo_santa)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    
    match args.len() {
        1 => println!("Please provide input file."),
        2 => {
            let moves: String = fs::read_to_string(&args[1]).
                expect("Error reading input file.");
            let mut houses: HashMap<String, u32> = HashMap::new();
            houses = visited_houses(&moves, houses);
            println!("[Part 1] Number of houses that receive at least one present: {}", houses.keys().len());

            let (santa, robo_santa) = split_moves(&moves);
            let mut houses: HashMap<String, u32> = HashMap::new();
            houses = visited_houses(&santa, houses);
            houses = visited_houses(&robo_santa, houses);
            println!("[Part 2] Number of houses that receive at least one present: {}", houses.keys().len());

        },
        _ => println!("Too many arguments!"),
    }
}

#[test]
fn test_part2() {
    let moves = String::from("^v^v^v^v^v");
    let (santa, robo_santa) = split_moves(&moves);
    assert_eq!(santa, "^^^^^");
    assert_eq!(robo_santa, "vvvvv");
    let mut houses: HashMap<String, u32> = HashMap::new();
    houses = visited_houses(&santa, houses);
    houses = visited_houses(&robo_santa, houses);
    assert_eq!(houses.keys().len(), 11);

    let moves = String::from("^>v<");
    let (santa, robo_santa) = split_moves(&moves);
    assert_eq!(santa, "^v");
    assert_eq!(robo_santa, "><");
    let mut houses: HashMap<String, u32> = HashMap::new();
    houses = visited_houses(&santa, houses);
    houses = visited_houses(&robo_santa, houses);
    assert_eq!(houses.keys().len(), 3);
}