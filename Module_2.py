# Variables and interactive programs
from random import randint
from math import pi

class Task_1:
    """
    Write a program that asks your name and then greets you by your name
    """
    @staticmethod
    def main() -> None:
        print("Module 2, Task 1.\n")
        name:str = input("Enter your name: ")
        print(f"Hello, {name}")
    
class Task_2:
    """
    Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
    """
    @staticmethod
    def main() -> None:
        print("Module 2, Task 2.\n")
        circle_radius:float = float(input("Enter the radius of a circle: "))
        circle_area = pi * circle_radius ** 2
        print(f"The area of the circle is: {circle_area}")

class Task_3:
    """
    Write a program that asks the user for the length and width of a rectangle.
    The program then prints out the perimeter and area of the rectangle.
    """
    @staticmethod
    def main() -> None:
        print("Module 2, Task 3.\n")
        rect_width:float = float(input("Enter the width of a rectangle: "))
        rect_height:float = float(input("Enter the height of a rectangle: "))
        rect_perimeter:float = (rect_height * 2) + (rect_width * 2)
        rect_area: float = rect_width * rect_height
        print(f"The perimeter of the rectangle is: {rect_perimeter}")
        print(f"The area of the rectangle is: {rect_area}")

class Task_4:
    """
    Write a program that asks the user for three integer numbers.
    The program prints out the sum, product, and average of the numbers.
    """
    @staticmethod
    def main() -> None:
        print("Module 2, Task 4.\n")
        print("Enter 3 numbers to compute the results")
        opr_value_1 = int(input("Enter the first number: "))
        opr_value_2 = int(input("Enter the second number: "))
        opr_value_3 = int(input("Enter the third number: "))
        opr_sum = opr_value_1 + opr_value_2 + opr_value_3
        opr_product = opr_value_1 * opr_value_2 * opr_value_3
        opr_average = opr_sum / 3
        print("Results: ")
        print(f"  Sum: {opr_sum}")
        print(f"  Product: {opr_product}")
        print(f"  Average: {opr_average}")

class Task_5:
    """
    Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots.
    The program converts the input to full kilograms and grams and outputs the result to the user.
    """
    @staticmethod
    def main() -> None:
        print("Module 2, Task 5.\n")
        LOT_IN_GRAMS:float = 13.3
        POUND_IN_LOTS:int = 32
        TALENT_IN_POUNDS:int = 20
        talents:int = int(input("Enter the number of talents: "))
        pounds:int = int(input("Enter the number of pounds: "))
        lots:int = int(input("Enter the number of lots: "))
        total_lots:int = (talents * TALENT_IN_POUNDS * POUND_IN_LOTS) + (pounds * POUND_IN_LOTS) + lots
        total_grams:float = total_lots * LOT_IN_GRAMS
        kilograms:int = int(total_grams // 1000)
        grams:float = total_grams % 1000
        print(f"Converted mass: {kilograms} kilograms and {grams:.2f} grams")

class Task_6:
    """
    Write a program that draws two random combinations of numbers for a combination lock:
        - a 3-digit code where each number is between 0 and 9.
        - a 4-digit code where each number is between 1 and 6.
    """ 
    @staticmethod
    def main() -> None:
        print("Module 2, Task 6.\n")
        code_3_digits:list[int] = [randint(0, 9) for _ in range(3)]
        code_4_digits:list[int] = [randint(1, 6) for _ in range(4)]
        print("Generated combination codes:")
        print(f"  3-digit code (0-9): {''.join(map(str, code_3_digits))}")
        print(f"  4-digit code (1-6): {''.join(map(str, code_4_digits))}")