# Using external interfaces
import requests

class Task_1:
    """
    Write a program that fetches and prints out a random Chuck Norris joke for the user.
    Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.
    """
    API_URL = "https://api.chucknorris.io/jokes/random"

    @staticmethod
    def get_joke() -> str:
        try:
            response = requests.get(Task_1.API_URL, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data.get("value", "No joke found.")
        except requests.exceptions.RequestException as e:
            return f"Error fetching joke: {e}"

    @staticmethod
    def main() -> None:
        print("Module 12, Task 1.\n")
        joke = Task_1.get_joke()
        print("Chuck Norris Joke:")
        print(joke)

class Task_2:
    """
    Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
    Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding
    weather condition description text and temperature in Celsius degrees.
    Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests.
    Furthermore, find out how you can convert Kelvin degrees into Celsius.
    """
    API_KEY = "API_KEY"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(city: str):
        try:
            params = {"q": city, "appid": Task_2.API_KEY}
            response = requests.get(Task_2.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            description = data["weather"][0]["description"]
            kelvin_temp = data["main"]["temp"]
            celsius_temp = kelvin_temp - 273.15
            return description, round(celsius_temp, 1)
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather: {e}", None
        except KeyError:
            return "Invalid response from API (check city name).", None

    @staticmethod
    def main() -> None:
        print("Module 12, Task 2.\n")
        city = input("Enter municipality name: ").strip()
        description, temp = Task_2.get_weather(city)
        if temp is not None:
            print(f"Weather in {city}: {description}, {temp}°C")
        else:
            print(description)