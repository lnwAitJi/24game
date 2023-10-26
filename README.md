# 24 Game Solver

This is a simple Python program that generates four random numbers and challenges the player to solve the "24 Game," where the goal is to use these numbers with basic arithmetic operations (+, -, *, /) to achieve a result of 24.

## Features

- Randomly generates four numbers between 1 and 9.
- Checks if a solution exists to make 24 using the given numbers.
- Allows the player to input their solution.
- Handles basic arithmetic operations (+, -, *, /).
- Provides feedback on whether the solution is correct.
- Offers the option to show the computer's solution if the player fails.

## Usage

1. Run the `main()` function in the script.
2. You will be presented with four random numbers.
3. You need to use these numbers with basic arithmetic operations to reach the target number, which is 24.
4. Input the slot number (1 to 4) where you want to use a number.
5. Input the slot number (1 to 4) where you want to apply an arithmetic operation (+, -, *, /).
6. Input the slot number (1 to 4) where you want to use another number.
7. The program will calculate the result and provide feedback.
8. If you run out of numbers, you can try again or see the computer's solution.

## Example

Here's an example of how to play the 24 Game using the script:

```plaintext
×——————————————————————————————————×
Generating numbers, please wait..

Solution found for (7:8:2:4) ✓
×——————————————————————————————————×

24 Game:
Slot | Number
 | 7
 | 8
 | 2
 | 4

[Calculate: [_ _ _ = __]
Enter your number
> 7

×——————————————————————————————————×
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy the game!
