# List structures and iterative loops (for)
from random import randint

class Task_1:
    """
    Write a program that asks the user how many dice to roll.
    The program rolls all the dice once and prints out the sum of the numbers.
    """
    @staticmethod
    def main() -> None:
        print("Module 5, Task 1.\n")
        dice_count:int = int(input("Enter how many dice to roll: "))
        total:int = 0
        for _ in range(dice_count):
            roll:int = randint(1, 6)
            total += roll
        print(f"Sum of {dice_count} dice rolls: {total}")

class Task_2:
    """
    Write a program that asks the user to enter numbers until they input an empty string to quit.
    At the end, the program prints out the five greatest numbers sorted in descending order.
    """
    @staticmethod
    def main() -> None:
        print("Module 5, Task 2.\n")
        numbers:list[int] = []

        while True:
            entry:str = input("Enter a number (empty string to quit): ")
            if entry == "":
                break
            try:
                number:int = int(entry)
                numbers.append(number)
            except ValueError:
                print("Invalid input, please enter an integer.")

        if numbers:
            numbers.sort(reverse=True)
            top_five:list[int] = numbers[:5]
            print("Top five numbers in descending order:")
            for n in top_five:
                print(n)
        else:
            print("No numbers were entered.")

class Task_3:
    """
    Write a program that asks the user for an integer and tells if the number is a prime number.
    Prime numbers are numbers that are only divisible by one or the number itself.
    """
    @staticmethod
    def main() -> None:
        print("Module 5, Task 3.\n")
        number:int = int(input("Enter an integer: "))
        if number < 2:
            print(f"{number} is not a prime number.")
            return

        is_prime: bool = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

class Task_4:
    """
    Write a program that asks the user to enter the names of five cities one by one and stores them into a list structure.
    Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
    """
    @staticmethod
    def main() -> None:
        print("Module 5, Task 4.\n")
        cities: list[str] = []
        for i in range(1, 6):
            city: str = input(f"Enter city {i}: ")
            cities.append(city)
        print("\nCities you entered:")
        for city in cities:
            print(city)