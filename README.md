# Exercises
![JavaScript](https://img.shields.io/badge/javascript-ES6-F0DB4F?style=for-the-badge&logo=javascript&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)

This repository contains exercises implemented in **JavaScript** and **Python**, organized into modules with individual tasks.

## JavaScript Exercises

The exercises for this section are located in the **`JavaScript/`** directory.

### Live Demo

Explore the JavaScript exercises directly on GitHub Pages:

[**Visit the Live Demo**](https://devbytamir.github.io/Exercises)

### Structure

- `index.html` - Main entry point for running exercises.  
- `scripts/` - Contains modules and shared helper functions:
    - `Helper.js` - Common utility functions.
    - `Module_1.js` ... `Module_4.js` - Individual exercise modules.
- `styles/` - CSS styles for the exercises.  
- `assets/` - Images and icons used by the exercises.

### Usage (Local)

1. Open **`JavaScript/index.html`** in a web browser.  
2. Use the interface to select and execute tasks from each module.  
3. View the output area for results.

## Python Exercises

The exercises for this section are located in the **`Python/`** directory.

### Structure

- `Module_1.py` ... `Module_13.py` - Individual exercise modules.  
- Tasks are implemented as **classes** (e.g., `Task_1`, `Task_2`).  
- Each class provides a **static method** `.main()` to execute the task.

### Dependencies

Install the required Python libraries using `pip`:

```bash
pip install mysql-connector-python flask requests geopy
```

### Usage

Import a task class from its module and execute it.

**Example:** Running Task 1 from Module 8:

```python
from Python.Module_8 import Task_1

Task_1.main()
```

### Notes

- Each task can be executed independently.  
- Replace placeholders for database credentials or API keys where indicated.