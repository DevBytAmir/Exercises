# While loops (while)
from random import randint, uniform

class Task_1:
    """
    Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
    """
    @staticmethod
    def main() -> None:
        print("Module 4, Task 1.\n")
        number:int = 1
        while number <= 1000:
            if number % 3 == 0:
                print(number)
            number += 1

class Task_2:
    """
    Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
    """
    @staticmethod
    def main() -> None:
        print("Module 4, Task 2.\n")
        while True:
            inches:float = float(input("Enter length in inches (negative value to quit): "))
            if inches < 0:
                print("Program ended.")
                break
            centimeters:float = inches * 2.54
            print(f"{inches} inches is {centimeters:.2f} cm")

class Task_3:
    """
    Write a program that asks the user to enter numbers until they enter an empty string to quit.
    Finally, the program prints out the smallest and largest number from the numbers it received.
    """
    @staticmethod
    def main() -> None:
        print("Module 4, Task 3.\n")
        numbers:list[float] = []
        while True:
            entry:str = input("Enter a number (empty string to quit): ")
            if entry == "":
                break
            try:
                number:float = float(entry)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        if numbers:
            print(f"Smallest number: {min(numbers)}")
            print(f"Largest number: {max(numbers)}")
        else:
            print("No numbers were entered.")

class Task_4:
    """
    Write a game where the computer draws a random integer between 1 and 10.
    The user tries to guess the number until they guess the right number.
    After each guess the program prints out a text: Too high, Too low or Correct.
    """
    @staticmethod
    def main() -> None:
        print("Module 4, Task 4.\n")
        secret:int = randint(1, 10)

        while True:
            try:
                guess:int = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if guess < secret:
                print("Too low.")
            elif guess > secret:
                print("Too high.")
            else:
                print("Correct. You guessed the number.")
                break

class Task_5:
    """
    Write a program that asks the user for a username and password.
    If either or both are incorrect, the program ask the user to enter the username and password again.
    This continues until the login information is correct or wrong credentials have been entered five times.
    If the information is correct, the program prints out Welcome.
    After five failed attempts the program prints out Access denied. The correct username is python and password rules.
    """
    @staticmethod
    def main() -> None:
        print("Module 4, Task 5.\n")
        correct_username:str = 'python'
        correct_password:str = 'rules'
        attempts:int = 0
        max_attempts:int = 5

        while attempts < max_attempts:
            username:str = input("Enter username: ")
            password:str = input("Enter password: ")
            if username == correct_username and password == correct_password:
                print("Welcome.")
                return
            else:
                attempts += 1
                remaining:int = max_attempts - attempts
                if remaining > 0:
                    print(f"Incorrect credentials. You have {remaining} attempts left.\n")
        print("Access denied.")

class Task_6:
    """
    Implement an algorithm for calculating an approximation for the value of pi.
    """
    @staticmethod
    def main() -> None:
        print("Module 4, Task 6.\n")
        points_amount:int = int(input("Enter the number of random points to generate: "))
        inside_circle:int = 0
        count: int = 0

        while count < points_amount:
            x:float = uniform(-1, 1)
            y:float = uniform(-1, 1)
            if x**2 + y**2 < 1:
                inside_circle += 1
            count += 1
        pi_approx:float = 4 * inside_circle / points_amount
        print(f"Approximation of pi with {points_amount} points: {pi_approx}")