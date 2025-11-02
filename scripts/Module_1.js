/**
 * Main Module 1 Tasks class
 */
class ModuleOneTasks {
    /** @param {Helper} helper - The shared Helper instance. */
    constructor(helper) {
        this.helper = helper;
    }

    /** Task 1: Print a simple message to the output panel. */
    task1() {
        this.helper.clearOutput();
        this.helper.printLine("I'm printing to the output.");
    }

    /** Task 2: Prompt for a name and greet the user. */
    task2() {
        this.helper.clearOutput();
        const name = prompt("Enter your name:")?.trim();

        if (!name) {
            alert("Name cannot be empty. Cancelling task.");
            return;
        }

        this.helper.printLine(`Hello, ${name}.`);
    }

    /** Task 3: Calculate sum, product, and average of three numbers. */
    task3() {
        this.helper.clearOutput();
        const nums = ["first", "second", "third"].map(label => this.helper.requestNumber(`Enter ${label} number:`));

        if (nums.includes(null)) {
            this.helper.printLine("Calculation cancelled.");
            return;
        }

        const [a, b, c] = nums;
        const sum = a + b + c;
        const product = a * b * c;
        const average = (sum / 3).toFixed(2); 

        this.helper.printLine(`You entered the numbers: ${a}, ${b}, and ${c}.`);
        this.helper.printLine("---");

        this.helper.printLine(`Sum: ${sum}`);
        this.helper.printLine(`Product: ${product}`);
        this.helper.printLine(`Average: ${average}`);
    }

    /** Task 4: Randomly assign a student to a fantasy house. */
    task4() {
        this.helper.clearOutput();
        const name = prompt("Enter student name:")?.trim();

        if (!name) {
            alert("Name cannot be empty. Cancelling task.");
            return;
        }

        const houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];
        const house = houses[Math.floor(Math.random() * houses.length)];
        this.helper.printLine(`${name}, you have been assigned to ${house}.`);
    }

    /** Task 5: Check if a given year is a leap year. */
    task5() {
        this.helper.clearOutput();
        const year = this.helper.requestNumber("Enter a year:");

        if (year === null) {
            this.helper.printLine("Task cancelled by user.");
            return;
        }

        const isLeap = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
        this.helper.printLine(`${year} is ${isLeap ? "a" : "not a"} leap year.`);
    }

    /** Task 6: Calculate the square root of a non-negative number. */
    task6() {
        this.helper.clearOutput();

        if (!confirm("Should I calculate the square root?")) {
            return this.helper.printLine("Calculation cancelled by user confirmation.");
        }

        const num = this.helper.requestNumber("Enter a number:");

        if (num === null) {
            this.helper.printLine("Task cancelled by user.");
            return;
        }

        if (num < 0) {
            return this.helper.printLine("The square root of a negative number is not defined in real numbers.");
        }
        
        this.helper.printLine(`Square root of ${num}: ${Math.sqrt(num)}`);
    }

    /** Task 7: Roll a specified number of dice and report the total sum. */
    task7() {
        this.helper.clearOutput();
        const rolls = this.helper.requestNumber("How many dice (positive integer)?");
        
        if (!Number.isInteger(rolls) || rolls <= 0) {
            alert("Please enter a positive integer for the number of dice.");
            return this.helper.printLine("Invalid input. Task cancelled.");
        }

        let total = 0;
        for (let i = 0; i < rolls; i++) {
            total += this.helper.rollDice();
        }

        this.helper.printLine(`Sum of ${rolls} dice rolls: ${total}`);
    }

    /** Task 8: Find and list all leap years within a given range. */
    task8() {
        this.helper.clearOutput();
        const start = this.helper.requestNumber("Enter start year:");
        const end = this.helper.requestNumber("Enter end year:");

        if (start === null || end === null) {
            this.helper.printLine("Task cancelled.");
            return;
        }

        if (start > end) {
            alert("Start year must be before or the same as the end year.");
            return this.helper.printLine("Invalid year range. Task aborted.");
        }

        const leapYears = [];
        for (let y = start; y <= end; y++) {
            if ((y % 4 === 0 && y % 100 !== 0) || y % 400 === 0) {
                leapYears.push(y);
            }
        }
        if (leapYears.length === 0) {
            this.helper.printLine(`No leap years found between ${start} and ${end}.`);
            return; 
        }
        this.helper.printLine(`Leap years between ${start} and ${end}:`); 
        this.helper.printList(leapYears);
    }

    /** Task 9: Check if an integer is a prime number. */
    task9() {
        this.helper.clearOutput();
        const num = this.helper.requestNumber("Enter an integer (>= 2):");

        if (num === null) {
            this.helper.printLine("Task cancelled by user.");
            return;
        }
        
        if (!Number.isInteger(num) || num < 2) {
            return this.helper.printLine(`${num} is not considered a prime number.`);
        }
        
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                return this.helper.printLine(`${num} is not a prime number (divisible by ${i}).`);
            }
        }
        
        this.helper.printLine(`${num} is a prime number.`);
    }

    /** Task 10: Simulate dice rolls and calculate the probability of a target sum. */
    task10() {
        this.helper.clearOutput();
        const dice = this.helper.requestNumber("Number of dice (e.g., 2):");
        const target = this.helper.requestNumber("Target sum (e.g., 7):");

        if (dice === null || target === null) {
            this.helper.printLine("Task cancelled by user.");
            return;
        }
        
        if (!Number.isInteger(dice) || dice < 1 || !Number.isInteger(target) || target < dice || target > dice * 6) {
            alert("Invalid dice or target sum for 6-sided dice.");
            return this.helper.printLine("Invalid input. Task cancelled.");
        }

        const trials = 10000;
        let success = 0;

        this.helper.printLine(`Simulating ${trials} trials for ${dice} dice to hit a target sum of ${target}.`);
        for (let i = 0; i < trials; i++) {
            let sum = 0;
            for (let d = 0; d < dice; d++) {
                sum += this.helper.rollDice();
            }
            if (sum === target) success++;
        }

        const probability = ((success / trials) * 100).toFixed(2);
        this.helper.printLine(`Estimated probability of rolling a total of ${target} with ${dice} dice: ${probability}%`);
    }
}
