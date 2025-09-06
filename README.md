
 ✅ To-Do List (Command Line App)

A simple **command-line To-Do List application** built in Python.
It allows you to **add, update, delete, and view tasks** while saving them in a JSON file for persistence.



 ✨ Features

* **Add tasks** to your to-do list.
* **Show all tasks** with numbering.
* **Update tasks** by selecting task number.
* **Delete tasks** easily.
* **Persistent storage** → tasks are saved in a `tasks.json` file.



 🚀 Usage

 Run the Program

Make sure you have **Python 3** installed, then run:


python todo.py


 Example Run


---------Simple To-Do List (type show, add, update, delete, exit)---------
Enter command: add
Enter task to add: Finish homework
Task added!

Enter command: add
Enter task to add: Read a book
Task added!

Enter command: show

Your To-Do List:
1. Finish homework
2. Read a book

Enter command: update
Your To-Do List:
1. Finish homework
2. Read a book
Enter task number to update: 1
Enter new task: Complete math assignment
Task updated!

Enter command: delete
Your To-Do List:
1. Complete math assignment
2. Read a book
Enter task number to delete: 2
Task deleted!

Enter command: exit
Goodbye!




 📂 Project Structure


todo-list/
│-- todo.py       # Main program file
│-- tasks.json    # Stores saved tasks
│-- README.md     # Documentation




 🛠️ Future Improvements

* Add **task completion status** (done/undone).
* Add **due dates and priorities**.
* Search/filter tasks.
* Build a **GUI version** using Tkinter or PyQt.
* Sync tasks with a **database or cloud storage**.




