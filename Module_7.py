# Tuple, set, and dictionary
class Task_1:
    """
    Write a program that asks the user for a number of a month and then prints out the corresponding season.
    Save the seasons as strings into a tuple in your program.
    We can define each season to last three months, December being the first month of winter.
    """
    @staticmethod
    def main() -> None:
        print("Module 7, Task 1.\n")
        seasons: tuple[str, str, str, str] = ("Winter", "Spring", "Summer", "Autumn")
        month: int = int(input("Enter the number of a month (1-12): "))

        if month < 1 or month > 12:
            print("Invalid month number. Please enter a number between 1 and 12.")
            return

        if month in (12, 1, 2):
            season = seasons[0]
        elif month in (3, 4, 5):
            season = seasons[1]
        elif month in (6, 7, 8):
            season = seasons[2]
        else:
            season = seasons[3]
        print(f"Month {month} corresponds to {season}.")

class Task_2:
    """
    Write a program that asks the user to enter names until he/she enters an empty string.
    After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
    Finally, the program lists out the input names one by one,
    one below another in any order. Use the set data structure to store the names.
    """
    @staticmethod
    def main() -> None:
        print("Module 7, Task 2.\n")
        names_set: set[str] = set()

        while True:
            name: str = input("Enter a name (empty string to quit): ")
            if name == "":
                break
            if name in names_set:
                print("Existing name")
            else:
                print("New name")
                names_set.add(name)

        print("\nAll names entered:")
        for n in names_set:
            print(n)

class Task_3:
    """
    Write a program for fetching and storing airport data.
    The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
    If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
    If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.
    If the user chooses to quit, the program execution ends.
    The user can choose a new option as many times they want until they choose to quit.
    """
    @staticmethod
    def main() -> None:
        print("Module 7, Task 3.\n")
        airports: dict[str, str] = {}

        while True:
            print("\nOptions:")
            print("1 - Enter a new airport")
            print("2 - Fetch airport information")
            print("3 - Quit")

            choice: str = input("Choose an option (1, 2, 3): ").strip()

            if choice == "1":
                icao: str = input("Enter ICAO code: ").upper().strip()
                if icao in airports:
                    print(f"Airport with ICAO {icao} already exists: {airports[icao]}")
                else:
                    name: str = input("Enter airport name: ").strip()
                    airports[icao] = name
                    print(f"Airport {name} with ICAO {icao} added.")

            elif choice == "2":
                icao: str = input("Enter ICAO code to fetch: ").upper().strip()
                if icao in airports:
                    print(f"Airport {icao}: {airports[icao]}")
                else:
                    print(f"No airport found with ICAO code {icao}.")

            elif choice == "3":
                print("Program ended.")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")