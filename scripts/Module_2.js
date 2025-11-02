/**
 * Main Module 2 Tasks class
 */
class ModuleTwoTasks {
    /** @param {Helper} helper - The shared Helper instance. */
    constructor(helper) {
        this.helper = helper;
    }

    /** Task 1: Request 5 numbers and print them in reverse order. */
    task1() {
        this.helper.clearOutput();
        const numbers = [];
        const requiredCount = 5;

        for (let i = 0; i < requiredCount; i++) {
            const n = this.helper.requestNumber(`Enter number ${i + 1}:`);
            if (n === null) {
                this.helper.printLine("Task cancelled by user.");
                return;
            }
            numbers.push(n);
        }

        this.helper.printLine("Numbers in reverse order:");
        for (let i = numbers.length - 1; i >= 0; i--) {
            this.helper.printLine(numbers[i]);
        }
    }

    /** Task 2: Collect participant names, sort alphabetically, and print as an ordered list. */
    task2() {
        this.helper.clearOutput();
        const count = this.helper.requestNumber("Enter the number of participants:");

        if (count === null || !Number.isInteger(count) || count <= 0) {
            this.helper.printLine("Invalid or cancelled input for participant count.");
            return;
        }

        const names = [];
        for (let i = 0; i < count; i++) {
            const name = prompt(`Enter name of participant ${i + 1}:`)?.trim();
            if (!name) {
                alert("Name cannot be empty, stopping input.");
                return;
            }
            names.push(name);
        }
        names.sort();
        this.helper.printLine("Participants (A-Z):");
        this.helper.printList(names, true); 
    }

    /** Task 3: Collect 6 dog names, sort them in reverse alphabetical order, and print as an unordered list. */
    task3() {
        this.helper.clearOutput();
        const dogs = [];
        const requiredCount = 6;

        for (let i = 0; i < requiredCount; i++) {
            const name = prompt(`Enter dog name ${i + 1}:`)?.trim();
            if (!name) {
                alert("Name cannot be empty, stopping input.");
                return;
            }
            dogs.push(name);
        }

        dogs.sort().reverse();
        this.helper.printLine("Dog Names (Z-A):");
        this.helper.printList(dogs);
    }

    /** Task 4: Collect numbers from the user until zero is entered, then print sorted descending. */
    task4() {
        this.helper.clearOutput();
        const numbers = [];
        let i = 1;

        while (true) {
            const n = this.helper.requestNumber(`Enter number ${i} (0 to stop):`);

            if (n === null) {
                this.helper.printLine("Task cancelled by user.");
                return;
            }
            
            if (n === 0) {
                break;
            }
        
            numbers.push(n);
            i++;
        }
        numbers.sort((a, b) => b - a);
        this.helper.printLine("Numbers from largest to smallest:");
        this.helper.printList(numbers);
    }

    /** Task 5: Collect numbers until a duplicate is entered, then print the unique numbers sorted ascending. */
    task5() {
        this.helper.clearOutput();
        const numbers = [];
        let i = 1;

        while (true) {
            const n = this.helper.requestNumber(`Enter number ${i}:`);
            
            if (n === null) {
                this.helper.printLine("Task cancelled by user.");
                return;
            }
            
            if (numbers.includes(n)) {
                alert(`The number ${n} was already entered. Stopping input.`);
                break;
            }

            numbers.push(n);
            i++;
        }

        numbers.sort((a, b) => a - b);
        this.helper.printLine("Unique numbers entered (ascending order):");
        this.helper.printList(numbers);
    }

    /** Task 6: Simulate rolling a 6-sided die until a 6 is rolled, printing all results as a list. */
    task6() {
        this.helper.clearOutput();
        const rolls = [];
        
        this.helper.printLine("Rolling a 6-sided die until a 6 is rolled...");

        while (true) {
            const roll = this.helper.rollDice(); 
            rolls.push(roll);
            
            if (roll === 6) {
                break;
            }
        }
        
        this.helper.printLine(`Finished in ${rolls.length} rolls.`);
        this.helper.printList(rolls);
    }

    /** Task 7: Simulate rolling an N-sided die until the maximum value (N) is rolled, printing all results. */
    task7() {
        this.helper.clearOutput();
        const sides = this.helper.requestNumber("Enter number of sides (N):");
        
        if (sides === null || !Number.isInteger(sides) || sides < 2) {
            this.helper.printLine("Invalid input. Sides must be an integer greater than 1.");
            return;
        }
        
        const rolls = [];
        const rollDice = () => Math.floor(Math.random() * sides) + 1;
        
        this.helper.printLine(`Rolling a ${sides}-sided die until ${sides} is rolled...`);
        
        while (true) {
            const roll = rollDice();
            rolls.push(roll);
            
            if (roll === sides) {
                break;
            }
        }

        this.helper.printLine(`Finished in ${rolls.length} rolls.`);
        this.helper.printList(rolls);
    }

    /** Task 8: Concatenate all strings in an array into a single string. */
    task8() {
        this.helper.clearOutput();
        const arr = ["Johnny", "DeeDee", "Joey", "Marky"];
        let result = "";
        for (let i = 0; i < arr.length; i++) {
            result += arr[i];
        }
        this.helper.printLine("Original array: " + arr.join(", "));
        this.helper.printLine(`Concatenated string: ${result}`);
    }

    /** Task 9: Filter an array to return only the even numbers. */
    task9() {
        this.helper.clearOutput();
        const arr = [2, 7, 4, 1, 9, 8];
        const evens = this.helper.even(arr); 
        this.helper.printLine("Original array: " + arr.join(", "));
        this.helper.printLine("Even numbers: " + evens.join(", "));
    }

    /** Task 10: Simulate a voting program, tallying votes and declaring the winner. */
    task10() {
        this.helper.clearOutput();
        const candidateCount = this.helper.requestNumber("Enter number of candidates:");
        
        if (candidateCount === null || !Number.isInteger(candidateCount) || candidateCount <= 0) {
            this.helper.printLine("Invalid or cancelled candidate count.");
            return;
        }

        const candidates = [];
        for (let i = 0; i < candidateCount; i++) {
            const name = prompt(`Enter candidate ${i + 1} name:`)?.trim();
            if (!name) {
                alert("Candidate name cannot be empty, stopping input.");
                return;
            }
            candidates.push({ name: name, votes: 0 });
        }

        const voterCount = this.helper.requestNumber("Enter number of voters:");
        if (voterCount === null || !Number.isInteger(voterCount) || voterCount < 0) {
            this.helper.printLine("Invalid or cancelled voter count.");
            return;
        }
        
        this.helper.printLine(`Starting voting with ${voterCount} voters for ${candidateCount} candidates.`);
        for (let i = 0; i < voterCount; i++) {
            const candidateNames = candidates.map(c => c.name).join(', ');
            const vote = prompt(`Voter ${i + 1}, enter a candidate name (${candidateNames}):`)?.trim();
            if (!vote) continue;
            const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
            
            if (candidate) {
                candidate.votes++;
            } else {
                this.helper.printLine(`Warning: Vote for "${vote}" by Voter ${i+1} was invalid and not counted.`);
            }
        }
        
        candidates.sort((a, b) => b.votes - a.votes);
        const winner = candidates[0];
        const tally = candidates.map(c => `${c.name}: ${c.votes} votes`);
        this.helper.printLine("--- Final Results ---");
        this.helper.printLine(`Winner: ${winner.name} (${winner.votes} votes)`);
        this.helper.printLine("--- Detailed Tally ---");
        this.helper.printList(tally);
    }
}
