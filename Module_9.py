# Fundamentals of object-oriented programming
from random import randint

class Car:
    """
    Task 1:
        Write a Car class that has the following properties:
            - registration number
            - maximum speed
            - current speed
            - travelled distance.
        Add a class initializer that sets the first two of the properties based on parameter values.
        The current speed and travelled distance of a new car must be automatically set to zero.

    Task 2:
        Extend the program by adding an accelerate method into the new class.
        The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed.
        The method must change the value of the speed property of the object.
        The speed of the car must stay below the set maximum and cannot be less than zero.

    Task 3:
        Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
        The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
    """
    def __init__(self, registration_number: str, max_speed: int):
        self.registration_number: str = registration_number
        self.max_speed: int = max_speed
        self.current_speed: int = 0
        self.travelled_distance: float = 0.0

    def accelerate(self, change: int) -> None:
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours: float) -> None:
        self.travelled_distance += self.current_speed * hours

    def __str__(self) -> str:
        return (f"Car {self.registration_number} | Max speed: {self.max_speed} km/h | Current speed: {self.current_speed} km/h | Travelled: {self.travelled_distance} km")

class Race:
    """
    Module 10, Task 4:
        Write a Race class that has the following properties: name, distance in kilometers, a list of cars participating in the race.
        The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class.
        The class has the following methods:
            - hour_passes: performs the operations done once per hour in the original exercise.
            - print_status: prints out the current information of each car as a clear, formatted table.
            - race_finished: which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
    """
    def __init__(self, name: str, distance: float, cars: list[Car]):
        self.name: str = name
        self.distance: float = distance
        self.cars: list[Car] = cars

    def hour_passes(self) -> None:
        for car in self.cars:
            car.accelerate(randint(-10, 15))
            car.drive(1)

    def print_status(self) -> None:
        print(f"\n{'='*50}")
        print(f"Race: {self.name}")
        print(f"{'Car':<10}{'Max Speed':<12}{'Speed':<10}{'Distance':<12}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.max_speed:<12}"
                  f"{car.current_speed:<10}{int(car.travelled_distance):<12}")
        print("-"*50)

    def race_finished(self) -> bool:
        return any(car.travelled_distance >= self.distance for car in self.cars)

class ElectricCar(Car):
    """
    Module 11, Task 2:
        Extend the previously written Car class by adding the subclasse GasolineCar.
        Electric cars have the capacity of the battery in kilowatt-hours as their property.
        Write initializers for the subclasses.
        For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
        It calls the initializer of the base class to set the first two properties and then sets its capacity.
    """
    def __init__(self, registration_number: str, max_speed: int, battery_capacity: float):
        Car.__init__(self, registration_number, max_speed)
        self.battery_capacity: float = battery_capacity

class GasolineCar(Car):
    """
    Module 11, Task 2:
        Extend the previously written Car class by adding the subclasse GasolineCar.
        Gasoline cars have the volume of the tank in liters as their property.
        Write initializers for the subclasses.
    """
    def __init__(self, registration_number: str, max_speed: int, tank_volume: float):
        Car.__init__(self, registration_number, max_speed)
        self.tank_volume: float = tank_volume

class Task_1:
    """
    Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
    Finally, print out all the properties of the new car.
    """
    @staticmethod
    def main() -> None:
        print("Module 9, Task 1.\n")
        car = Car("ABC-123", 142)
        print(car)

class Task_2:
    """
    Extend the main program so that the speed of the car is first increased by +30 km/h,
    then +70 km/h and finally +50 km/h. Then print out the current speed of the car.
    Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
    """
    @staticmethod
    def main() -> None:
        print("Module 9, Task 2.\n")
        car = Car("ABC-123", 142)
        car.accelerate(30)
        car.accelerate(70)
        car.accelerate(50)
        print(f"Current speed after acceleration: {car.current_speed} km/h")
        car.accelerate(-200)
        print(f"Speed after emergency brake: {car.current_speed} km/h")

class Task_3:
    """
    The travelled distance of car object is 2000 km. The current speed is 60 km/h.
    Method call car.drive(1.5) increases the travelled distance to 2090 km.
    """
    @staticmethod
    def main() -> None:
        print("Module 9, Task 3.\n")
        car = Car("ABC-123", 142)
        car.current_speed = 60
        car.travelled_distance = 2000
        car.drive(1.5)
        print(f"Travelled distance after driving: {car.travelled_distance} km")

class Task_4:
    """
    At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
    The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
    The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
    One per every hour of the race, the following operations are performed:
        - The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accelerate method.
        - Each car is made to drive for one hour. This is done with the drive method.
        - The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.
    """
    @staticmethod
    def main() -> None:
        print("Module 9, Task 4.\n")
        cars = []
        for i in range(1, 11):
            max_speed = randint(100, 200)
            registration_number = f"ABC-{i}"
            cars.append(Car(registration_number, max_speed))

        race_distance = 10000
        hour = 0

        while not any(car.travelled_distance >= race_distance for car in cars):
            hour += 1
            for car in cars:
                speed_change = randint(-10, 15)
                car.accelerate(speed_change)
                car.drive(1)

        print(f"\nRace finished after {hour} hours.\n")
        print(f"{'Car':<10}{'Max Speed':<12}{'Speed':<10}{'Distance':<12}")
        print("-" * 44)
        for car in cars:
            print(f"{car.registration_number:<10}{car.max_speed:<12}{car.current_speed:<10}{int(car.travelled_distance):<12}")

class Task_4_Module_10:
    """
    Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
    The new race is given a list of ten cars similarly to the earlier exercise.
    The main program simulates the progressing of the race by calling the hour_passes in a loop,
    after which it uses the race_finished method to check if the race has finished.
    The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
    """
    @staticmethod
    def main() -> None:
        print("Module 10, Task 4.\n")
        cars = [Car(f"ABC-{i+1}", randint(100, 200)) for i in range(10)]
        race = Race("Grand Demolition Derby", 8000, cars)
        hour = 0

        while not race.race_finished():
            hour += 1
            race.hour_passes()
            if hour % 10 == 0:
                print(f"\nStatus after {hour} hours:")
                race.print_status()

        print(f"\nRace finished after {hour} hours.")
        race.print_status()

class Task_2_Module_11:
    """
    Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3).
    Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
    """
    @staticmethod
    def main() -> None:
        print("Module 11, Task 2.\n")
        electric = ElectricCar("ABC-15", 180, 52.5)
        gasoline = GasolineCar("ACD-123", 165, 32.3)
        electric.accelerate(120)
        gasoline.accelerate(100)
        electric.drive(3)
        gasoline.drive(3)
        print(f"Electric car {electric.registration_number} travelled {electric.travelled_distance} km")
        print(f"Gasoline car {gasoline.registration_number} travelled {gasoline.travelled_distance} km")