/**
 * Main Module 3 Tasks class
 */
class ModuleThreeTasks {
    #picArray = [
        {
            title: 'Title 1',
            caption: 'Caption 1',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
            image: {
                large: 'assets/image_1.jpg',
                medium: 'assets/thumbnail_1.jpg',
            },
        },
        {
            title: 'Title 2',
            caption: 'Caption 2',
            description: 'Donec dignissim tincidunt nisl...',
            image: {
                large: 'assets/image_2.jpg',
                medium: 'assets/thumbnail_2.jpg',
            },
        },
        {
            title: 'Title 3',
            caption: 'Caption 3',
            description: 'Phasellus imperdiet nunc...',
            image: {
                large: 'assets/image_3.jpg',
                medium: 'assets/thumbnail_3.jpg',
            },
        },
        {
            title: 'Title 4',
            caption: 'Caption 4',
            description: 'Duis sodales enim eget leo condimentum...',
            image: {
                large: 'assets/image_4.jpg',
                medium: 'assets/thumbnail_4.jpg',
            },
        },
        {
            title: 'Title 5',
            caption: 'Caption 5',
            description: 'Sed vel velit ante. Aenean quis viverra magna...',
            image: {
                large: 'assets/image_5.jpg',
                medium: 'assets/thumbnail_5.jpg',
            },
        },
        {
            title: 'Title 6',
            caption: 'Caption 6',
            description: 'Sed vel velit ante. Aenean quis viverra magna...',
            image: {
                large: 'assets/image_6.jpg',
                medium: 'assets/thumbnail_6.jpg',
            },
        },
        {
            title: 'Title 7',
            caption: 'Caption 7',
            description: 'Lorem ipsum dolor sit amet...',
            image: {
                large: 'assets/image_7.jpg',
                medium: 'assets/thumbnail_7.jpg',
            },
        },
        {
            title: 'Title 8',
            caption: 'Caption 8',
            description: 'Praesent eget cursus urna...',
            image: {
                large: 'assets/image_8.jpg',
                medium: 'assets/thumbnail_8.jpg',
            },
        },
        {
            title: 'Title 9',
            caption: 'Caption 9',
            description: 'Praesent eget cursus urna...',
            image: {
                large: 'assets/image_9.jpg',
                medium: 'assets/thumbnail_9.jpg',
            },
        },
    ];

    /** @param {Helper} helper - The shared Helper instance. */
    constructor(helper) {
        this.helper = helper;
    }
    
    /** Task 1: Add list items and a class to #target using innerHTML. */
    task1() {
        this.helper.clearOutput();
        const target = this.helper.listTargetElement;

        target.innerHTML = `<li>First item</li><li>Second item</li><li>Third item</li>`;
        target.classList.add("my-list");
        this.helper.printLine("List items added and class 'my-list' applied to #target.");
    }

    /** Task 2: Add list items using createElement and appendChild. */
    task2() {
        this.helper.clearOutput();
        const target = this.helper.listTargetElement;

        const li1 = document.createElement("li");
        li1.textContent = "First item";

        const li2 = document.createElement("li");
        li2.textContent = "Second item";
        li2.classList.add("my-item");
        
        const li3 = document.createElement("li");
        li3.textContent = "Third item";

        target.appendChild(li1);
        target.appendChild(li2);
        target.appendChild(li3);

        this.helper.printLine("List items created via createElement, and second item has class 'my-item'.");
    }

    /** Task 3: Add list items using innerHTML property in a for-loop. */
    task3() {
        this.helper.clearOutput();
        const target = this.helper.listTargetElement;
        const names = ["John", "Paul", "Jones"];

        let listItemsHTML = ''; 
        
        for (let i = 0; i < names.length; i++) {
            listItemsHTML += `<li>${names[i]}</li>`;
        }
        
        target.innerHTML = listItemsHTML;
        this.helper.printLine("Names added to list using innerHTML property in a loop.");
    }

    /** Task 4: Add <option> elements using createElement and appendChild. */
    task4() {
        this.helper.clearOutput();
        const target = this.helper.listTargetElement;

        const students = [
            { name: "John", id: "2345768" },
            { name: "Paul", id: "2134657" },
            { name: "Jones", id: "5423679" }
        ];

        target.innerHTML = '';

        const select = document.createElement("select");
        select.id = "student-select";

        for (let student of students) {
            const option = document.createElement("option");
            option.value = student.id;
            option.textContent = student.name;
            select.appendChild(option);
        }
        target.appendChild(select);
        this.helper.printLine("Student options added to select menu.");
    }

    /** Task 5: Add article cards. */
    task5() {
        this.helper.clearOutput();
        const section = this.helper.articleTargetElement;
        section.innerHTML = '';

        for (const item of this.#picArray) { 
            const articleCard = this.helper.createArticleCard(item);
            section.appendChild(articleCard);
        }
    }

    /** Task 6: Creates a button that triggers an alert when clicked. */
    task6() {

        this.helper.clearOutput();
        const alertButton = document.createElement('button');
        alertButton.textContent = "Click Me To Alert";
        alertButton.addEventListener("click", () => alert("Button clicked."));
        this.helper.outputElement.appendChild(alertButton);
        this.helper.printLine("Click the button above to see the alert.");
    }

    /** Task 7: Make a hover effect with JavaScript to swap an image source. */
    task7() {
        this.helper.clearOutput();
        this.helper.printLine("Hover over the text to change the image.");

        const container = this.helper.outputElement; 
        
        const defaultImage = "assets/image_2.jpg";
        const hoverImage = "assets/image_3.jpg";
        const triggerText = "Hover over me";

        const img = document.createElement("img");
        img.id = "hoverImage";
        img.src = defaultImage;
        img.alt = "Hover Example";
        img.classList.add("hover-image-display");

        const p = document.createElement("p");
        p.id = "hoverTrigger";
        p.textContent = triggerText;
        p.classList.add("hover-trigger-style");

        p.addEventListener("mouseover", () => {
            img.src = hoverImage;
        });
        
        p.addEventListener("mouseout", () => {
            img.src = defaultImage;
        });

        container.appendChild(p);
        container.appendChild(img);
    }

    /** Task 8: Creates an interactive calculator form using two inputs, a select dropdown, and a button. */
    task8() {
        this.helper.clearOutput(); 
        this.helper.printLine("Enter numbers and choose an operation.");

        const container = this.helper.outputElement;
        const calculatorWrapper = document.createElement("div");
        calculatorWrapper.classList.add("calculator-ui");

        const input1 = document.createElement("input");
        input1.id = "num1";
        input1.type = "number"; 
        input1.placeholder = "Enter first number";
        input1.classList.add("calc-input");

        const input2 = document.createElement("input");
        input2.id = "num2";
        input2.type = "number";
        input2.placeholder = "Enter second number";
        input2.classList.add("calc-input"); 

        const select = document.createElement("select");
        select.id = "operation";
        select.classList.add("calc-input");

        const operations = [
            { value: "add", text: "Addition" },
            { value: "sub", text: "Subtraction" },
            { value: "multi", text: "Multiplication" },
            { value: "div", text: "Division" },
        ];

        operations.forEach(op => {
            const option = document.createElement("option");
            option.value = op.value;
            option.textContent = op.text;
            select.appendChild(option);
        });

        const button = document.createElement("button");
        button.textContent = "Calculate";

        const result = document.createElement("p");
        
        button.addEventListener("click", () => {
            const num1 = input1.valueAsNumber; 
            const num2 = input2.valueAsNumber;

            if (isNaN(num1) || isNaN(num2)) {
                result.textContent = "Please enter valid numbers.";
                return;
            }

            let res;
            switch (select.value) {
                case "add": res = num1 + num2; break;
                case "sub": res = num1 - num2; break;
                case "multi": res = num1 * num2; break;
                case "div":
                    if (num2 === 0) {
                        res = "Cannot divide by zero.";
                    } else {
                        res = num1 / num2;
                    }
                    break;
            }
            result.textContent = "Result: " + res;
        });

        calculatorWrapper.appendChild(input1);
        calculatorWrapper.appendChild(input2);
        calculatorWrapper.appendChild(select);
        calculatorWrapper.appendChild(button);
        calculatorWrapper.appendChild(result);
        container.appendChild(calculatorWrapper);
    }

    /** Task 9: Creates a single-field calculator that parses an input string. */
    task9() {
        this.helper.clearOutput();
        this.helper.printLine("Enter a calculation below (e.g., 3+5, 2-78).");

        const container = this.helper.outputElement;
        const calculatorWrapper = document.createElement("div");
        calculatorWrapper.classList.add("calculator-ui");

        const input = document.createElement("input");
        input.type = "text";
        input.id = "calcInput";
        input.placeholder = "e.g. 3+5";
        input.classList.add("calc-input-line"); 
        
        const button = document.createElement("button");
        button.textContent = "Calculate";
        button.classList.add("calc-button-line");

        const result = document.createElement("p");

        button.addEventListener("click", () => {
            const value = input.value.trim();
            const operators = ["+", "-", "*", "/"];
            let foundOperator = null;

            for (const op of operators) {
                if (value.includes(op)) {
                    foundOperator = op;
                    break;
                }
            }

            if (!foundOperator) {
                result.textContent = "Invalid input. Use format: number+operator+number.";
                return;
            }
            const parts = value.split(foundOperator);
            if (parts.length !== 2) {
                result.textContent = "Invalid format. Ensure only one operator is used.";
                return;
            }
            const num1 = Number(parts[0].trim());
            const num2 = Number(parts[1].trim());

            if (isNaN(num1) || isNaN(num2)) {
                result.textContent = "Please enter valid integers.";
                return;
            }

            let res;
            switch (foundOperator) {
                case "+": res = num1 + num2; break;
                case "-": res = num1 - num2; break;
                case "*": res = num1 * num2; break;
                case "/": 
                    if (num2 === 0) {
                        res = "Cannot divide by zero.";
                    } else {
                        res = Math.trunc(num1 / num2); 
                    }
                    break;
            }

            result.textContent = `Result: ${res}`;
        });

        calculatorWrapper.appendChild(input);
        calculatorWrapper.appendChild(button);
        calculatorWrapper.appendChild(result);
        container.appendChild(calculatorWrapper);
    }

    /** Task 10: Reads first name and last name values from a form and prints them to the output. */
    task10() {
        this.helper.clearOutput();
        const outputContainer = this.helper.outputElement;
        
        this.helper.printLine("Enter first and last name below.");

        const form = document.createElement("form");
        form.id = "name-form-dynamic";

        const firstName = document.createElement("input");
        firstName.type = "text";
        firstName.name = "firstname";
        firstName.placeholder = "First Name";

        const lastName = document.createElement("input");
        lastName.type = "text";
        lastName.name = "lastname";
        lastName.placeholder = "Last Name";

        const submit = document.createElement("button");
        submit.type = "submit";
        submit.textContent = "Print Name";

        const result = this.helper.listTargetElement;

        form.appendChild(firstName);
        form.appendChild(lastName);
        form.appendChild(submit);

        outputContainer.appendChild(form);
        outputContainer.appendChild(result);

        form.addEventListener("submit", (e) => {
            e.preventDefault();
            const fNameValue = form.querySelector("input[name='firstname']").value.trim();
            const lNameValue = form.querySelector("input[name='lastname']").value.trim();

            if (fNameValue && lNameValue) {
                result.textContent = `Your name is ${fNameValue} ${lNameValue}`;
            } else {
                result.textContent = "Please enter both first and last name.";
            }
        });
    }

    /** Task 11: Creates article cards and adds click handlers to open the large image in a modal. */
    task11() {
        this.helper.clearOutput();
        const section = this.helper.articleTargetElement;

        const modal = document.querySelector("dialog");
        const modalImg = modal.querySelector("img");
        const modalClose = modal.querySelector("span");

        modalClose.addEventListener("click", () => {
            modal.classList.remove("is-open");
            setTimeout(() => {modal.close();}, 300); 
        });
        
        modal.addEventListener("click", (event) => {
            if (event.target === modal) {
                modal.classList.remove("is-open");
                setTimeout(() => {
                    modal.close();
                }, 300);
            }
        });

        for (const item of this.#picArray) {
            const article = this.helper.createArticleCard(item); 
            article.addEventListener("click", () => {
                modalImg.src = item.image.large; 
                modalImg.alt = item.title; 
                modal.showModal(); 
                setTimeout(() => {
                    modal.classList.add("is-open"); 
                }, 0); 
            });
            section.appendChild(article);
        }
    }
}
