#include <iostream> // This is like opening a toolbox for input/output tasks.

int main() { // This is where our program starts talking.

    // Let's introduce two variables (containers for numbers).
    int num1, num2;

    // Politely ask the user to enter two numbers.
    std::cout << "Enter the first number: ";
    std::cin >> num1; // The user types the first number.

    std::cout << "Enter the second number: ";
    std::cin >> num2; // The user types the second number.

    // Let's do the math (add the two numbers).
    int sum = num1 + num2;

    // Share the result with the user.
    std::cout << "The sum is: " << sum << std::endl;

    return 0; // Tell the computer that everything went well.
}
