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


## ▶️ Usage
The main entry point for the application is:
```
python todo_app.py COMMAND
```
### 1. Add a New Task
```
python todo_app.py add "Finish assignment"
```
You will be prompted for:
- Deadline date (`dd/mm/yyyy`)
- Time (`HH:MM`)
Example:
``` 
deadline?(dd/mm/yyy): 22/02/2025
at?(HH:MM): 17:00
```
### 2. View All Tasks
```
python todo_app.py read
```
Output example:
```
1. 22/02/2025 at 17:00 Finish assignment
Time left is : 1 day, 5:32:10
```
If a task is overdue:
```
Overdue
```
### 3. Delete a Task by Number
```
python todo_app.py delete 2
```
Deletes the second task in `tasks.txt`.


## 📚 API Overview
This project uses a single module:
#### `todo_app.py`
- `add(t: str)` → Add a task with deadline and time
- `read()` → Display tasks and remaining time
- `delete(num: int)` → Remove a task from storage
- Typer `app` object → Defines CLI commands

Because command logic is simple, the full CLI serves as the public API.


## 🗂️ Project Structure
```
ToDo-app-CLI/
│
├── todo_app.py          # Main CLI script (Typer app)
├── tasks.txt            # Auto-generated storage file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── ...
```


## 🤝 Contributing
Contributions are welcome!
If you'd like to improve functionality, documentation, or testing:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request with a clear description
