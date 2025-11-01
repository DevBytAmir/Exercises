# Setting up a backend service with an interface
import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify

class Task_1:
    """
    Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
    Use the prior prime number exercise as a starting point.
    For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31.
    The response must be in the format of {"Number":31, "isPrime":true}.
    """
    @staticmethod
    def is_prime(n):
            if n < 2:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    @staticmethod
    def main() -> None:
        print("Module 13, Task 1.\n")
        app = Flask(__name__)

        @app.route('/prime_number/<int:number>', methods=['GET'])
        def check_prime(number):
            result = {
                "Number": number,
                "isPrime": Task_1.is_prime(number)
            }
            return jsonify(result)

        app.run(debug=True)

class Task_2:
    """
    Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format.
    The information is fetched from the airport database used on this course.
    For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
    The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}
    """
    @staticmethod
    def main() -> None:
        print("Module 13, Task 2.\n")

        app = Flask(__name__)
        @app.route("/airport/<icao>", methods=["GET"])
        def get_airport(icao):
            connection = None
            cursor = None
            try:
                connection = mysql.connector.connect(
                        host='DB_HOST',
                        port=3306,
                        database='DB_NAME',
                        user='DB_USER',
                        password='DB_PASSWORD'
                    )
                cursor = connection.cursor(dictionary=True)
                query = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
                cursor.execute(query, (icao.upper(),))
                result = cursor.fetchone()
                if result:
                    return jsonify({
                        "ICAO": result["ident"],
                        "Name": result["name"],
                        "Location": result["municipality"]
                    })
                return jsonify({"error": f"No airport found with ICAO code {icao}"}), 404

            except Error as e:
                return jsonify({"error": str(e)}), 500

            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()

        app.run(debug=True)