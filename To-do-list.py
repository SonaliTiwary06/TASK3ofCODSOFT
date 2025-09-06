import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)  
        
# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])
    print()

# Add a task
def add_task(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!\n")

# Update a task
def update_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    num = int(input("Enter task number to update: "))
    if 1 <= num <= len(tasks):
        new_task = input("Enter new task: ")
        tasks[num - 1] = new_task
        save_tasks(tasks)
        print("Task updated!\n")
    else:
        print("Invalid task number!\n")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted!\n")
    else:
        print("Invalid task number!\n")

# Main program
def main():
    tasks = load_tasks()
    print("---------Simple To-Do List (type show, add, update, delete, exit)---------")
    while True:
        command = input("Enter command: ").lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "show":
            show_tasks(tasks)
        elif command == "add":
            add_task(tasks)
        elif command == "update":
            update_task(tasks)
        elif command == "delete":
            delete_task(tasks)
        else:
            print("Invalid command! Use show, add, update, delete, or exit.\n")

main()
