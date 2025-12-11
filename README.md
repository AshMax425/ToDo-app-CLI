# 📝 ToDo-app-CLI
A very simple and lightweight ToDo app using python that can be  used from the command line

## 📘Description
The ToDo CLI App is a lightweight task manager that allows users to add tasks with deadlines, view upcoming tasks, check overdue items, and delete tasks - all from the command line. It uses a plain text file for storage, making it portable, simple, and easy to run anywhere.

## ✨Features
- ➕ Add tasks with deadlines and times
- 📖 Read and display all tasks with their remaining time
- ⏰ Automatically calculates whether tasks are overdue
- 🗑️ Delete tasks by number
- 💾 Persistent storage in a text file (`tasks.txt`)
- ⚡ Fast CLI execution powered by Typer
- 🧩 Minimal dependencies and easy to install

## 🛠️ Installation
#### Prerequisites: 
- Python **3.8 or higher** installed. Use `python --version` to check.
- `pip` (included with Python)
- (Optional): A virtual environment for isolated dependencies

#### Installation Steps:

```bash
1. Clone repository and navigate to the project directory:
    - git clone https://github.com/nilesh-sengupta/ToDo-app-CLI.git
    - cd ToDo-app-CLI

2. Create and activate virtual environment (optional but recommended)
    - python -m venv .venv
    - source .venv/bin/activate  # Mac/Linux  
    - source .venv\Scripts\activate  # Windows

3. Install dependencies
    - pip install -r requirements.txt
    - If `requirements.txt` does not exist, create it with:
        - pip install typer
        - pip freeze > requirements.txt
```