import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, description):
    tasks.append({'title': title, 'description': description, 'completed': False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_task_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed successfully!")
    else:
        print("Invalid task number.")

def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {'Completed' if task['completed'] else 'Incomplete'}")
    if not tasks:
        print("No tasks found.")

def delete_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    print("Welcome to Task Manager!\n")
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View All Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            view_tasks(tasks)
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(tasks, task_number)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            view_tasks(tasks)
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
