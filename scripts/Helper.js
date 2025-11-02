/**
 * Helper class to manage output and validated user input for all modules.
 */
class Helper {
    /**
     * @param {string} outputId - ID of the primary DOM element for general text/code results (e.g., "output").
     * @param {string} listTargetId - ID of the secondary DOM element for list results (e.g., "target").
     * @param {string} articleTargetId - ID of the tertiary DOM element for article/image results (e.g., "pictures").
     */
    constructor(outputId, listTargetId, articleTargetId) {
        this.outputElement = document.getElementById(outputId);
        this.listTargetElement = document.getElementById(listTargetId);
        this.articleTargetElement = document.getElementById(articleTargetId);
        this.cleanerButton = document.getElementById('clean-output-btn');

        if (!this.outputElement || !this.listTargetElement || !this.articleTargetElement) {
            console.error("Helper initialization failed: One or more required output DOM elements were not found.");
            return;
        }
    }

    /** Clears all dynamic content from the output area while keeping persistent targets. */
    clearOutput() {
        this.listTargetElement.innerHTML = "";
        this.articleTargetElement.innerHTML = "";
    
        let child = this.outputElement.lastElementChild;
        while (child) {
            const prevChild = child.previousElementSibling;
            const isPersistentElement = 
                (child.id === this.listTargetElement.id) || 
                (child.id === this.articleTargetElement.id);

            if (!isPersistentElement) {
                this.outputElement.removeChild(child);
            }
            child = prevChild;
        }
    }

    /**
     * Prints a line of text inside a paragraph element.
     * @param {string} text
     */
    printLine(text) {
        const p = document.createElement('p');
        p.textContent = text;
        this.outputElement.appendChild(p);
    }
    
    /**
     * Prints a list of items as either an ordered or unordered list.
     * @param {Array<string|number>} items
     * @param {boolean} [ordered=false] - Use an ordered list (<ol>) if true.
     */
    printList(items, ordered = false) {
        const tag = ordered ? 'ol' : 'ul';
        const listElement = document.createElement(tag);
        const fragment = document.createDocumentFragment();

        items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = String(item); 
            fragment.appendChild(li);
        });
        
        listElement.appendChild(fragment); 
        this.outputElement.appendChild(listElement);
    }

    /**
     * Prompts the user for a number and validates input.
     * @param {string} message
     * @returns {number|null}
     */
    requestNumber(message) {
        const raw = prompt(message);
        if (raw === null) return null;
        const num = Number(raw);
        if (isNaN(num)) {
            alert("Invalid number. Please try again.");
            return null;
        }
        return num;
    }

    /**
     * Creates and returns a single article card element from data.
     * @param {object} item - The data object for a single picture card.
     * @param {string} item.title - The title of the card.
     * @param {string} item.caption - The figure caption.
     * @param {string} item.description - The main article description.
     * @param {object} item.image - Object containing image URLs.
     * @param {string} item.image.medium - The URL for the thumbnail image.
     * @returns {HTMLElement} The fully constructed <article> element.
     */
    createArticleCard(item) {
        const article = document.createElement("article");
        article.classList.add("card");

        const h2 = document.createElement("h2");
        h2.textContent = item.title;

        const figure = document.createElement("figure");
        const img = document.createElement("img");
        img.src = item.image.medium;
        img.alt = item.title;

        const figcaption = document.createElement("figcaption");
        figcaption.textContent = item.caption;

        const p = document.createElement("p");
        p.textContent = item.description;

        figure.appendChild(img);
        figure.appendChild(figcaption);
        article.appendChild(h2);
        article.appendChild(figure);
        article.appendChild(p);

        return article;
    }

    /** Rolls a fair six-sided dice. */
    rollDice() {
        return Math.floor(Math.random() * 6) + 1;
    }

    /**
     * Receives an array of numbers and returns only the even ones.
     * @param {number[]} arr - The input array.
     * @returns {number[]} - The array containing only even numbers.
     */
    even(arr) {
        const evenNumbers = [];
        for (const num of arr) {
            if (num % 2 === 0) {
                evenNumbers.push(num);
            }
        }
        return evenNumbers;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const headers = document.querySelectorAll(".modules-column h2");

    const first = headers[0];
    if (first) first.classList.add("open");

    headers.forEach(header => {
        header.addEventListener("click", () => {
            headers.forEach(h => { if (h !== header) h.classList.remove("open");});
            header.classList.toggle("open");
        });
    });
});
