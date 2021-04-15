use std::env;
use std::fs;
use std::collections::HashMap;

macro_rules! stringify {
    ($tuple: expr) => {
        String::from(format!("{}:{}", $tuple.0, $tuple.1));
    };
}

fn visited_houses(moves: &String) -> u32 {
    let mut houses: HashMap<String, u32> = HashMap::new();
    let mut position: (i32, i32) = (0, 0);
    houses.insert(stringify!(position), 1);
    for _move in moves.chars() {
        match _move {
            '^' => position.1 += 1,
            'v' => position.1 -= 1,
            '>' => position.0 += 1,
            '<' => position.0 -= 1,
            _ => println!("Error! Move must be ^ v > <.")
        }
        *houses.entry(stringify!(position)).or_insert(1) += 1;
    }
    houses.keys().len() as u32
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
            let houses = visited_houses(&moves);
            println!("[Part 1] Number of houses that receive at least one present: {}", houses);

            let (santa, robo_santa) = split_moves(&moves);
            let santa_houses = visited_houses(&santa);
            println!("Santa visited: {}", santa_houses);
            let robo_santa_houses = visited_houses(&robo_santa);
            println!("Robo-santa visited: {}", robo_santa_houses);
            println!("[Part 2] Number of houses that receive at least one present: {}", santa_houses + robo_santa_houses - 1);

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
    let santa_houses = visited_houses(&santa);
    assert_eq!(santa_houses, 6);
    let robo_houses = visited_houses(&robo_santa);
    assert_eq!(robo_houses, 6);

    let moves = String::from("^>v<");
    let (santa, robo_santa) = split_moves(&moves);
    assert_eq!(santa, "^v");
    assert_eq!(robo_santa, "><");
    let santa_houses = visited_houses(&santa);
    assert_eq!(santa_houses, 2);
    let robo_houses = visited_houses(&robo_santa);
    assert_eq!(robo_houses, 2);
}