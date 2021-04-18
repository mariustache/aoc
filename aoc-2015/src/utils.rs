// Utils: functions, macros, etc. used in most of the exercises.

#[macro_export]
macro_rules! solution {
    ($part: expr, $res: expr) => {
        println!("[Part {}] Solution is: {}", $part, $res)
    };
}