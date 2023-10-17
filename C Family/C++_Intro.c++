
#include <iostream>

int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}

#include <iostream>

int main() {
    // Declare a variable to store the user's age
    int age;

    // Prompt the user to enter their age
    std::cout << "Please enter your age: ";

    // Read the user's input and store it in the age variable
    std::cin >> age;

    // Use an if statement to check if the user is old enough to vote
    if (age >= 18) {
        std::cout << "You are old enough to vote!" << std::endl;
    } else {
        std::cout << "You are not old enough to vote yet." << std::endl;
    }

    return 0;
}