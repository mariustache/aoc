use std::env;
use std::fs;

struct Box {
    length: u32,
    width: u32,
    height: u32
}

fn box_area(_box: &Box) -> u32 {
    let prod1 = _box.length * _box.width;
    let prod2 = _box.width * _box.height;
    let prod3 = _box.height * _box.length;
    let result = prod1 + prod2 + prod3;
    let prod_vec = vec![prod1, prod2, prod3];
    
    2 * result + prod_vec.iter().min().unwrap()
}

fn ribbon_needed(_box: &Box) -> u32 {
    let mut dimensions = vec![_box.length, _box.width, _box.height];
    dimensions.sort();
    let mut ribbon = 0;
    for dimension in &dimensions[..dimensions.len() - 1] {
        ribbon += 2 * dimension;
    }
    
    ribbon + (_box.length * _box.height * _box.width)
}

fn obtain_box(dimensions: Vec<&str>) -> Box {
    assert_eq!(dimensions.len(), 3);
    let string_to_u32 = |dim: &str| -> u32 { dim.parse().unwrap() };
    Box {
        length: string_to_u32(&dimensions[0]),
        width: string_to_u32(&dimensions[1]),
        height: string_to_u32(&dimensions[2])
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        1 => println!("Please provide input file!"),
        2 => {
            let dimensions: String = fs::read_to_string(&args[1])
                .expect("Error reading input file!");
            
            let mut total_paper: u32 = 0;
            let mut total_ribbon: u32 = 0;

            for dimension in dimensions.lines() {
                let _box: Box = obtain_box(dimension.split("x").collect());
                total_paper += box_area(&_box);
                total_ribbon += ribbon_needed(&_box);
            }
            println!("[Part 1] Square feet of wrapping paper to order: {}", total_paper);
            println!("[Part 2] Feet of ribbon to order: {}", total_ribbon);
        },
        _ => println!("Too many arguments")
    }
}

#[test]
fn test_part2() {
    let mut _box = Box {
        length: 2,
        width: 3,
        height: 4
    };

    let total_ribbon = ribbon_needed(&_box);
    assert_eq!(total_ribbon, 34, "Total ribbon for 2x3x4: {}", total_ribbon);

    _box.length = 1;
    _box.width = 1;
    _box.height = 10;

    let total_ribbon = ribbon_needed(&_box);
    assert_eq!(total_ribbon, 14, "Total ribbon for 1x1x10: {}", total_ribbon);
}

