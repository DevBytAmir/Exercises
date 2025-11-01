# Conditional structures (if)
class Task_1:
    """
    Write a program that asks a fisher the length of a zander in centimeters.
    If the zander does not fulfill the size limit, the program instructs to release the fish back
    into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
    A zander must be 42 centimeters or longer to meet the size limit.
    """
    @staticmethod
    def main() -> None:
        print("Module 3, Task 1.\n")
        SIZE_LIMIT:int = 42
        zander_length:int = int(input("Enter the length of the zander in cm: "))
        if zander_length < SIZE_LIMIT:
            shortfall:int = SIZE_LIMIT - zander_length
            print(f"The zander is {shortfall} cm below the size limit. Release it back into the lake.")
        else:
            print("The zander meets the size limit.")

class Task_2:
    """
    Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below.
    You must use an if/elif/else structure in your solution.
        - LUX: upper-deck cabin with a balcony.
        - A: above the car deck, equipped with a window.
        - B: windowless cabin above the car deck.
        - C: windowless cabin below the car deck.
    """
    @staticmethod
    def main() -> None:
        print("Module 3, Task 2.\n")
        cabin:str = input("Enter the cabin class (LUX, A, B, C): ").strip().upper()
        if cabin == "LUX":
            print("LUX: upper-deck cabin with a balcony.")
        elif cabin == "A":
            print("A: above the car deck, equipped with a window.")
        elif cabin == "B":
            print("B: windowless cabin above the car deck.")
        elif cabin == "C":
            print("C: windowless cabin below the car deck.")
        else:
            print("Invalid cabin class.")

class Task_3:
    """
    Write a program that asks for the biological gender and hemoglobin value (g/l).
    The program the notifies the user if the hemoglobin value is low, normal or high.
        - A normal hemoglobin value for adult females is between 117-155 g/l.
        - A normal hemoglobin value for adult males is between 134-167 g/l.
    """
    @staticmethod
    def main() -> None:
        print("Module 3, Task 3.\n")
        gender:str = input("Enter your biological gender (male/female): ").lower()
        hemoglobin:float = float(input("Enter your hemoglobin value (g/l): "))
        if gender == "female":
            if hemoglobin < 117:
                print("Your hemoglobin value is low.")
            elif hemoglobin <= 155:
                print("Your hemoglobin value is normal.")
            else:
                print("Your hemoglobin value is high.")

        elif gender == "male":
            if hemoglobin < 134:
                print("Your hemoglobin value is low.")
            elif hemoglobin <= 167:
                print("Your hemoglobin value is normal.")
            else:
                print("Your hemoglobin value is high.")

        else:
            print("Invalid gender entered. Please enter 'male' or 'female'.")

class Task_4:
    """
    Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
    A year is a leap year if it is divisible by four.
    However, years divisible by 100 are leap years only if they are also divisible by 400.
    """
    @staticmethod
    def main() -> None:
        print("Module 3, Task 4.\n")
        year:int = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")