// This is a basic Rust program that prints "Hello, world!" to the console.
fn main() {
    // The `println!` macro is used to print text to the console.
    // The `!` indicates that this is a macro rather than a regular function.
    println!("Hello, world!");
    
    // Rust is a statically-typed language, which means that the type of a variable
    // must be declared at compile-time. Here's an example of declaring a variable:
    let x: i32 = 42;
    
    // The `let` keyword is used to declare a variable.
    // The `:` is used to specify the type of the variable.
    // In this case, `i32` is a 32-bit signed integer.
    // The `=` is used to assign a value to the variable.
    // In this case, the value is `42`.
    
    // Rust also has a concept of ownership and borrowing, which helps prevent
    // common programming errors like null pointer dereferences and memory leaks.
    // Here's an example of using a reference to borrow a value:
    let y: i32 = 10;
    let y_ref: &i32 = &y;
    
    // The `&` symbol is used to create a reference to a value.
    // In this case, `y_ref` is a reference to `y`.
    // References are read-only by default, which helps prevent accidental
    // modification of the original value.
    
    // Rust also has a powerful type system that allows for safe and expressive
    // abstractions. Here's an example of using a `struct` to define a custom type:
    struct Point {
        x: f64,
        y: f64,
    }
    
    // The `struct` keyword is used to define a new type.
    // In this case, `Point` is a struct with two fields: `x` and `y`.
    // The `f64` type is a 64-bit floating point number.
    
    // Rust also has a number of control flow constructs, like `if` statements and loops.
    // Here's an example of using an `if` statement to conditionally execute code:
    let z: i32 = 5;
    if z > 0 {
        println!("z is positive");
    } else if z < 0 {
        println!("z is negative");
    } else {
        println!("z is zero");
    }
    
    // The `if` keyword is used to start an `if` statement.
    // The condition is specified in parentheses.
    // The code to execute if the condition is true is enclosed in curly braces.
    // The `else if` and `else` keywords are used to specify alternative branches.
    
    // Finally, Rust has a powerful package manager called `cargo` that makes it easy
    // to manage dependencies and build projects. Here's an example of using `cargo`:
    // 1. Create a new Rust project with `cargo new my_project`.
    // 2. Add a dependency to the `rand` crate by adding `rand = "0.8.4"` to the `[dependencies]` section of `Cargo.toml`.
    // 3. Use the `rand` crate in your code with `use rand::Rng;` and `let random_number = rand::thread_rng().gen_range(1..=100);`.
}
