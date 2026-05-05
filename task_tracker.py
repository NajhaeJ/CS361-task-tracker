tasks = []


def show_menu():
    print("\nTask Tracker")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. More Details")
    print("5. Exit")


def add_task():
    task_name = input("Enter task: ")

    if task_name.strip() == "":
        print("Task cannot be empty.")
        return

    task = {
        "name": task_name,
        "complete": False
    }

    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task["complete"] else "Active"
        print(f"{index}. {task['name']} - {status}")


def mark_complete():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to mark complete: "))
        task_index = task_number - 1

        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return

        confirm = input("Are you sure? Type yes to confirm: ")

        if confirm.lower() == "yes":
            tasks[task_index]["complete"] = True
            print("Task marked complete.")
        else:
            print("Action cancelled.")

    except ValueError:
        print("Please enter a valid number.")


def more_details():
    print("\nMore Details")
    print("This app lets users add tasks, view tasks, and mark tasks as complete.")
    print("Users can avoid extra information by staying on the main menu.")
    print("Users can gather more information by choosing this More Details option.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            more_details()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-5.")


main()