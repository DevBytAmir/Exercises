# Using relational databases
import mysql.connector
from mysql.connector import Error
from geopy.distance import geodesic

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='DB_HOST',
            port=3306,
            database='DB_NAME',
            user='DB_USER',
            password='DB_PASSWORD'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

class Task_1:
    """
    Write a program that asks the user to enter the ICAO code of an airport.
    The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course.
    The ICAO codes are stored in the ident column of the airport table.
    """
    @staticmethod
    def main() -> None:
        print("Module 8, Task 1.\n")
        icao_code = input("Enter the ICAO code of the airport: ").upper().strip()
        connection = get_db_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT name, municipality FROM airport WHERE ident = %s"
            cursor.execute(query, (icao_code,))
            result = cursor.fetchone()
            if result:
                print(f"Airport Name: {result['name']}")
                print(f"Location (Town): {result['municipality']}")
            else:
                print(f"No airport found with ICAO code: {icao_code}")

        except Error as e:
            print(f"Error querying the database: {e}")
        finally:
            cursor.close()
            connection.close()
            print("Database connection closed.")

class Task_2:
    """
    Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type.
    """
    @staticmethod
    def main() -> None:
        print("Module 8, Task 2.\n")
        area_code = input("Enter the area code (e.g., FI): ").upper().strip()
        connection = get_db_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor(dictionary=True)
            query = """
            SELECT name, ident, type 
            FROM airport 
            WHERE iso_country = %s 
            ORDER BY type
            """
            cursor.execute(query, (area_code,))
            results = cursor.fetchall()
            if results:
                print(f"\nAirports in {area_code} ordered by type:\n")
                for row in results:
                    print(f"{row['name']} ({row['ident']}) - Type: {row['type']}")
            else:
                print(f"No airports found for area code: {area_code}")

        except Error as e:
            print(f"Error querying the database: {e}")
        finally:
            cursor.close()
            connection.close()
            print("\nDatabase connection closed.")

class Task_3:
    """
    Write a program that asks the user to enter the ICAO codes of two airports.
    The program prints out the distance between the two airports in kilometers.
    The calculation is based on the airport coordinates fetched from the database.
    Calculate the distance using the geopy library.
    """
    @staticmethod
    def main() -> None:
        print("Module 8, Task 3.\n")

        icao1 = input("Enter the ICAO code of the first airport: ").upper().strip()
        icao2 = input("Enter the ICAO code of the second airport: ").upper().strip()
        connection = get_db_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
            cursor.execute(query, (icao1,))
            airport1 = cursor.fetchone()
            if not airport1:
                print(f"No airport found with ICAO code: {icao1}")
                return

            cursor.execute(query, (icao2,))
            airport2 = cursor.fetchone()
            if not airport2:
                print(f"No airport found with ICAO code: {icao2}")
                return

            coords_1 = (airport1['latitude_deg'], airport1['longitude_deg'])
            coords_2 = (airport2['latitude_deg'], airport2['longitude_deg'])
            distance_km = geodesic(coords_1, coords_2).kilometers
            print( f"\nDistance between {airport1['name']} ({icao1}) and {airport2['name']} ({icao2}): {distance_km:.2f} km")

        except Error as e:
            print(f"Error querying the database: {e}")
        finally:
            cursor.close()
            connection.close()
            print("\nDatabase connection closed.")