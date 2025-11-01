/**
 * Main Module 4 Tasks class
 */
class ModuleFourTasks {
    static TVMAZE_URL = "https://api.tvmaze.com/search/shows?q=";
    static CHUCK_RANDOM_URL = "https://api.chucknorris.io/jokes/random";
    static CHUCK_SEARCH_URL = "https://api.chucknorris.io/jokes/search?query=";
    
    /** @param {Helper} helper - The shared Helper instance. */
    constructor(helper) {
        this.helper = helper;
    }

    /**
     * Creates a reusable search form UI.
     */
    #createSearchForm(placeholder, buttonText) {
        const wrapper = document.createElement("div");
        wrapper.classList.add("search-wrapper");

        const form = document.createElement("form");
        form.classList.add("search-form");

        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = placeholder;
        input.classList.add("search-input");

        const button = document.createElement("button");
        button.type = "submit";
        button.textContent = buttonText;
        button.classList.add("search-button");

        const resultsDiv = document.createElement("div");
        resultsDiv.classList.add("search-results");

        form.append(input, button);
        wrapper.append(form, resultsDiv);

        return { wrapper, form, input, resultsDiv };
    }

    /** Task 1: TV Series Search with AJAX */
    task1() {
        this.helper.clearOutput();
        this.helper.printLine("Enter a TV series name to search the TVMaze API.");

        const container = this.helper.outputElement;
        const { wrapper, form, input, resultsDiv } = this.#createSearchForm("Enter TV series name", "Search");
        container.appendChild(wrapper);


        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            const query = input.value.trim();
            resultsDiv.innerHTML = "";

            if (!query) {
                resultsDiv.textContent = "Please enter a TV series name.";
                return;
            }

            resultsDiv.textContent = "Searching...";
            try {
                const response = await fetch(`${ModuleFourTasks.TVMAZE_URL}${encodeURIComponent(query)}`);
                if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
                const data = await response.json();

                if (data.length === 0) {
                    resultsDiv.textContent = `No results found for "${query}".`;
                    return;
                }

                const pre = document.createElement("pre");
                pre.classList.add("json-output");
                pre.textContent = JSON.stringify(data, null, 2);
                resultsDiv.innerHTML = "";
                resultsDiv.appendChild(pre);

            } catch (error) {
                console.error("TVMaze Fetch Error:", error);
                resultsDiv.textContent = "Error fetching data. Check console for details.";
            }
        });
    }

    /** Task 2: TV Series Search - display results in the output. */
    task2() {
        this.helper.clearOutput();
        this.helper.printLine("Enter a TV series name and see results below.");

        const container = this.helper.outputElement;
        const { wrapper, form, input, resultsDiv } = this.#createSearchForm("Enter TV series name", "Search");
        container.appendChild(wrapper);

        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            const query = input.value.trim();
            resultsDiv.innerHTML = "";
            
            if (!query) {
                resultsDiv.textContent = "Please enter a TV series name.";
                return;
            }
            
            resultsDiv.textContent = "Searching...";

            try {
                const response = await fetch(`${ModuleFourTasks.TVMAZE_URL}${encodeURIComponent(query)}`);
                if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
                const data = await response.json();

                resultsDiv.innerHTML = "";

                if (data.length === 0) {
                    resultsDiv.textContent = `No results found for "${query}".`;
                    return;
                }

                data.forEach(({ show }) => {
                    const card = document.createElement("div");

                    if (show.image?.medium) {
                        const img = document.createElement("img");
                        img.src = show.image.medium;
                        img.alt = show.name;
                        card.appendChild(img);
                    }

                    const title = document.createElement("h3");
                    title.textContent = show.name;
                    card.appendChild(title);

                    const summary = document.createElement("p");
                    summary.innerHTML = show.summary || "No description available.";
                    card.appendChild(summary);

                    resultsDiv.appendChild(card);
                });

            } catch (error) {
                resultsDiv.textContent = "Error fetching data. Check console for details.";
                console.error("TVMaze Fetch Error:", error);
            }
        });
    }

    /** Task 3: Display detailed TV series info in articles */
    task3() {
        this.helper.clearOutput();
        this.helper.printLine("Enter a TV series name to see detailed results.");

        const container = this.helper.outputElement;
        const { wrapper, form, input, resultsDiv } = this.#createSearchForm("Enter TV series name", "Search");
        container.appendChild(wrapper);

        form.addEventListener("submit", async (e) => {
            e.preventDefault(); 
            const query = input.value.trim();
            resultsDiv.innerHTML = "Searching...";

            if (!query) {
                resultsDiv.textContent = "Please enter a TV series name.";
                return;
            }

            try {
                const response = await fetch(`${ModuleFourTasks.TVMAZE_URL}${encodeURIComponent(query)}`);
                if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
                const data = await response.json();

                resultsDiv.innerHTML = "";

                if (data.length === 0) {
                    resultsDiv.textContent = `No results found for "${query}".`;
                    return;
                }

                data.forEach(({ show }) => {
                    const article = document.createElement("article");
                    article.classList.add("show-article"); 

                    const h2 = document.createElement("h2");
                    h2.textContent = show.name;
                    article.appendChild(h2);

                    const link = document.createElement("a");
                    link.href = show.url;
                    link.textContent = "More details on TVMaze";
                    link.target = "_blank";
                    link.classList.add("show-link");
                    article.appendChild(link);

                    if (show.image?.medium) {
                        const img = document.createElement("img");
                        img.src = show.image.medium;
                        img.alt = show.name;
                        img.classList.add("show-image-medium"); 
                        article.appendChild(img);
                    }

                    const summary = document.createElement("div");
                    summary.innerHTML = show.summary || "No summary available.";
                    summary.classList.add("show-summary");
                    article.appendChild(summary);

                    resultsDiv.appendChild(article);
                });

            } catch (error) {
                resultsDiv.textContent = "Error fetching data. Check console for details.";
                console.error("TVMaze Fetch Error:", error);
            }
        });
    }

    /** Task 4: Display detailed TV series info with default images. */
    task4() {
        this.helper.clearOutput();
        this.helper.printLine("Enter a TV series name to see detailed results with default images.");

        const container = this.helper.outputElement;
        const { wrapper, form, input, resultsDiv } = this.#createSearchForm("Enter TV series name", "Search");
        container.appendChild(wrapper);

        form.addEventListener("submit", async (e) => {
            e.preventDefault(); 
            const query = input.value.trim();
            resultsDiv.innerHTML = "Searching..."; 

            if (!query) {
                resultsDiv.textContent = "Please enter a TV series name.";
                return;
            }

            try {
                const response = await fetch(`${ModuleFourTasks.TVMAZE_URL}${encodeURIComponent(query)}`);
                if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
                const data = await response.json();

                resultsDiv.innerHTML = ""; 

                if (data.length === 0) {
                    resultsDiv.textContent = `No results found for "${query}".`;
                    return;
                }

                data.forEach(({ show }) => {
                    const article = document.createElement("article");
                    article.classList.add("show-article"); 

                    const h2 = document.createElement("h2");
                    h2.textContent = show.name;
                    article.appendChild(h2);

                    const link = document.createElement("a");
                    link.href = show.url;
                    link.textContent = "More details on TVMaze";
                    link.target = "_blank";
                    link.classList.add("show-link");
                    article.appendChild(link);

                    const img = document.createElement("img");
                    img.src = show.image?.medium
                        ? show.image.medium
                        : "https://placehold.co/210x295?text=Not%20Found"; 
                    img.alt = show.name;
                    img.classList.add("show-image-medium"); 
                    article.appendChild(img);
 
                    const summary = document.createElement("div");
                    summary.innerHTML = show.summary || "No summary available.";
                    summary.classList.add("show-summary"); 
                    article.appendChild(summary);

                    resultsDiv.appendChild(article);
                });

            } catch (error) {
                resultsDiv.textContent = "Error fetching data. Check console for details.";
                console.error("TVMaze Fetch Error:", error);
            }
        });
    }

    /** Task 5: Fetches and displays a random Chuck Norris joke. */
    task5() {
        this.helper.clearOutput();
        this.helper.printLine("Fetching a random Chuck Norris joke...");

        (async () => {
            try {
                const response = await fetch(ModuleFourTasks.CHUCK_RANDOM_URL);
                if (!response.ok) throw new Error(`HTTP error: ${response.status}`);

                const data = await response.json();
                this.helper.printLine(`Chuck Norris Joke: ${data.value}`);
                
            } catch (error) {
                console.error("Chuck Norris Fetch Error:", error);
                this.helper.printLine("Error fetching joke. See console for details.");
            }
        })();
    }

    /** Task 6: Search Chuck Norris jokes by query. */
    task6() {
        this.helper.clearOutput();
        this.helper.printLine("Enter a search term to find Chuck Norris jokes.");

        const container = this.helper.outputElement;
        const { wrapper, form, input, resultsDiv } = this.#createSearchForm("Enter keyword (e.g. 'code', 'virus')", "Search Jokes");
        container.appendChild(wrapper);

        form.addEventListener("submit", async (e) => {
            e.preventDefault(); 
            const query = input.value.trim();
            resultsDiv.innerHTML = "Searching...";

            if (!query) {
                resultsDiv.textContent = "Please enter a search term.";
                return;
            }

            try {
                const response = await fetch(`${ModuleFourTasks.CHUCK_SEARCH_URL}${encodeURIComponent(query)}`);
                if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
                const data = await response.json();
                
                resultsDiv.innerHTML = "";

                if (data.total === 0) {
                    resultsDiv.textContent = `No jokes found for "${query}".`;
                    return;
                }

                data.result.forEach(joke => {
                    const article = document.createElement("article");
                    article.classList.add("joke-article"); 

                    const p = document.createElement("p");
                    p.textContent = joke.value;

                    article.appendChild(p);
                    resultsDiv.appendChild(article);
                });

            } catch (error) {
                resultsDiv.textContent = "Error fetching jokes. See console for details.";
                console.error("Chuck Norris Fetch Error:", error);
            }
        });
    }
}
