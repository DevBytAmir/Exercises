# Functions
from random import randint
from math import pi

class Task_1:
    """
    Write a function that returns a random dice roll between 1 and 6.
    Write a main program that rolls the dice until the result is 6.
    The main program should print out the result of each roll.
    """
    @staticmethod
    def func() -> int:
        return randint(1, 6)

    @staticmethod
    def main() -> None:
        print("Module 6, Task 1.\n")
        while True:
            result: int = Task_1.func()
            print(f"Rolled: {result}")
            if result == 6:
                print("Got a 6. Stopping.")
                break

class Task_2:
    """
    Modify the function above so that it gets the number of sides on the dice as a parameter.
    With the modified function you can for example roll a 21-sided role-playing dice.
    The difference to the last exercise is that the dice rolling in the main program continues
    until the program gets the maximum number on the dice, which is asked from the user at the beginning.
    """
    @staticmethod
    def func(sides: int) -> int:
        return randint(1, sides)

    @staticmethod
    def main() -> None:
        print("Module 6, Task 2.\n")
        sides: int = int(input("Enter the number of sides on the dice: "))
        max_value: int = sides

        while True:
            result: int = Task_2.func(sides)
            print(f"Rolled: {result}")
            if result == max_value:
                print(f"Got the maximum value {max_value}! Stopping.")
                break

class Task_3:
    """
    Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
    Write a main program that asks for a volume in gallons from the user and converts the value to liters.
    The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
    """
    @staticmethod
    def func(gallons: float) -> float:
        return gallons * 3.78541

    @staticmethod
    def main() -> None:
        print("Module 6, Task 3.\n")
        while True:
            gallons: float = float(input("Enter volume in gallons (negative to quit): "))
            if gallons < 0:
                print("Program ended.")
                break
            liters: float = Task_3.func(gallons)
            print(f"{gallons} gallons is {liters:.2f} liters.\n")

class Task_4:
    """
    Write a function that gets a list of integers as a parameter.
    The function returns the sum of all the numbers in the list.
    For testing, write a main program where you create a list, call the function, and print out the value it returned.
    """
    @staticmethod
    def func(numbers: list[int]) -> int:
        total: int = 0
        for num in numbers:
            total += num
        return total

    @staticmethod
    def main() -> None:
        print("Module 6, Task 4.\n")
        numbers: list[int] = [8, 16, 9, 2, 9]
        total: int = Task_4.func(numbers)
        print(f"The sum of the list {numbers} is {total}.")

class Task_5:
    """
    Write a function that gets a list of integers as a parameter.
    The function returns a second list that is otherwise the same as the original list except that all odd numbers have been removed.
    For testing, write a main program where you create a list, call the function,
    and then print out both the original as well as the cut-down list.
    """
    @staticmethod
    def func(numbers: list[int]) -> list[int]:
        new_list: list[int] = []
        for num in numbers:
            if num % 2 == 0:
                new_list.append(num)
        return new_list

    @staticmethod
    def main() -> None:
        print("Module 6, Task 5.\n")
        original_list: list[int] = [1, 4, 7, 10, 13, 16, 19]
        filtered_list: list[int] = Task_5.func(original_list)
        print(f"Original list: {original_list}")
        print(f"List without odd numbers: {filtered_list}")

class Task_6:
    """
    Write a function that receives two parameters:
        - the diameter of a round pizza in centimeters
        - the price of the pizza in euros.
    The function calculates and returns the unit price of the pizza per square meter.
    The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza
    provides better value for money.
    """
    @staticmethod
    def func(diameter_cm: float, price_eur: float) -> float:
        radius_m: float = (diameter_cm / 100) / 2
        area_m2: float = pi * radius_m ** 2
        unit_price: float = price_eur / area_m2
        return unit_price

    @staticmethod
    def main() -> None:
        print("Module 6, Task 6.\n")
        diameter1: float = float(input("Enter diameter of pizza 1 (cm): "))
        price1: float = float(input("Enter price of pizza 1 (euro): "))
        unit_price1: float = Task_6.func(diameter1, price1)

        diameter2: float = float(input("Enter diameter of pizza 2 (cm): "))
        price2: float = float(input("Enter price of pizza 2 (euro): "))
        unit_price2: float = Task_6.func(diameter2, price2)

        print(f"\nUnit price pizza 1: {unit_price1:.2f} euros per m^2")
        print(f"Unit price pizza 2: {unit_price2:.2f} euros per m^2")

        if unit_price1 < unit_price2:
            print("Pizza 1 provides better value for money.")
        elif unit_price2 < unit_price1:
            print("Pizza 2 provides better value for money.")
        else:
            print("Both pizzas have the same unit price.")