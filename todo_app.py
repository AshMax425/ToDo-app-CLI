"""
Command-line ToDo Application built with Typer.

This module exposes three commands:

1. add: Add a new task with a deadline.
2. read: Read all tasks and display time remaining or overdue status.
3. delete: Delete a task by its number in the list

Tasks are stored line-by-line in ``tasks.txt`` in the format:
    dd/mm/yyyy at HH:MM Task Description
"""

import typer
import datetime
from datetime import date
app=typer.Typer()
@app.command()
def add(t: str):
    """
    Add a new task with a deadline and time.

    This command interactively prompts the user for a deadline date and time,
    the appends a formatted line to ``tasks.txt``. The stored line includes
    the date, time, and text descpription of the task.
    
    Args:
        t (str): The task description to be added.

    Example:
        $ python todo_app.py add "Finish the report"
        deadline?(dd/mm/yyyy): 22/02/2025
        at?(HH:MM): 17:00
    """    
    time=''
    time = typer.prompt("deadline?(dd/mm/yyyy)")
    at=''
    at = typer.prompt("at?(HH:MM)")
    t=time+" at "+at+" "+t+'\n'
    file1=open("tasks.txt",'a')
    file1.write(t)
    file1.close()
@app.command()
def read():
    """
    Display all saved tasks and the time remaining until each deadline.

    Reads tasks from ``tasks.txt``, and prints each task with an index and either
    the time remaining or and "Ooverdue" status if the deadline has passed.

    Example:
        $ python todo_app.py read
        1.  22/02/2025 at 17:00 Finish the report
        Time left is: 1 day, 5:30:00
    """
    today1 = datetime.datetime.now()
    file1=open("tasks.txt",'r')
    res=file1.readlines()
    file1.close()
    for i in range(0,len(res)):
        u=res[i]
        d=int(u[0]+u[1])
        m=int(u[3]+u[4])
        y=int(u[6]+u[7]+u[8]+u[9])
        h=int(u[14]+u[15])
        min=int(u[17]+u[18])
        now=datetime.datetime(y,m,d,h,min)
        lefttime=str(now-today1)
        print((i+1),". ",res[i])
        if(lefttime[0]=="-"):
            print("Overdue")
        else:
            print("Time left is:",lefttime)
@app.command()
def delete(num: int):
    with open(r"tasks.txt", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            if number not in [num-1]:
                fp.write(line)
if __name__ == "__main__":
    app()
