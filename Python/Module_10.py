# Association
class Elevator:
    """
    Task 1:
        Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
        The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
        If you make elevator h for example the method call h.go_to_floor(5),
        the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
        The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
    """
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor: int = bottom_floor
        self.top_floor: int = top_floor
        self.current_floor: int = bottom_floor

    def floor_up(self) -> None:
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Elevator at floor {self.current_floor}")

    def floor_down(self) -> None:
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, floor: int) -> None:
        if floor < self.bottom_floor or floor > self.top_floor:
            print(f"Floor {floor} is out of range.")
            return
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

class Building:
    """
    Task 2:
        Extend the previous program by creating a Building class.
        The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
        When a building is created, the building creates the required number of elevators.
        The list of elevators is stored as a property of the building.
        Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.

    Task 3:
        Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor.
    """
    def __init__(self, bottom_floor: int, top_floor: int, num_elevators: int):
        self.bottom_floor: int = bottom_floor
        self.top_floor: int = top_floor
        self.elevators: list[Elevator] = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number: int, destination_floor: int) -> None:
        if 1 <= elevator_number <= len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {destination_floor}:")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)
        else:
            print(f"Invalid elevator number: {elevator_number}")

    def fire_alarm(self) -> None:
        print("\nFire alarm activated. Moving all elevators to the bottom floor.")
        for idx, elevator in enumerate(self.elevators, start=1):
            print(f"\nElevator {idx} moving to bottom floor:")
            elevator.go_to_floor(self.bottom_floor)

class Task_1:
    """
    Test the class by creating an elevator in the main program,
    tell it to move to a floor of your choice and then back to the bottom floor.
    """
    @staticmethod
    def main() -> None:
        print("Module 10, Task 1.\n")
        elevator = Elevator(0, 12)
        print("Going to floor 6:")
        elevator.go_to_floor(6)
        
        print("Returning to bottom floor:")
        elevator.go_to_floor(elevator.bottom_floor)

class Task_2:
    """
    In the main program, write the statements for creating a new building and running the elevators of the building.
    """
    @staticmethod
    def main() -> None:
        print("Module 10, Task 2.\n")
        building = Building(bottom_floor=0, top_floor=12, num_elevators=4)
        building.run_elevator(1, 11)
        building.run_elevator(2, 9)
        building.run_elevator(3, 2)
        building.run_elevator(4, building.bottom_floor)

class Task_3:
    """
    Continue the main program by causing a fire alarm in your building.
    """
    @staticmethod
    def main() -> None:
        print("Module 10, Task 3.\n")
        building = Building(bottom_floor=0, top_floor=12, num_elevators=4)
        building.run_elevator(1, 11)
        building.run_elevator(2, 9)
        building.run_elevator(3, 2)
        building.run_elevator(4, building.bottom_floor)
        building.fire_alarm()

class Task_4:
    """
    This Task is done in module 9
    """
    pass