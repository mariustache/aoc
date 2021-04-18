use std::env;
use std::fs;
use md5;

use utils::solution;

const NONCE5: usize = 5;
const NONCE6: usize = 6;

fn find_hash(secret_key: &String, nonce: usize) -> u32 {
    let leading_zeros: String = "0".repeat(nonce);
    let mut number: u32 = 1;
    loop {
        let mut input: String = String::from(secret_key);
        input.push_str(&number.to_string());
        let digest = md5::compute(&input);
        let md5hash = format!("{:x}", digest);
        //println!("Trying {}. Hash: {}", input, md5hash);

        if md5hash[..nonce] == leading_zeros {
            break
        }
        number += 1;
    }

    number
}

fn solve(data: &String) {
    let secret_key: String = fs::read_to_string(&data).
        expect("Error reading input file!");
    
    let solution: u32 = find_hash(&secret_key, NONCE5);
    solution!("1", solution);

    let solution: u32 = find_hash(&secret_key, NONCE6);
    solution!("2", solution);
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        1 => println!("Please provide input file."),
        2 => solve(&args[1]),
        _ => println!("Too many arguments!"),
    }
}