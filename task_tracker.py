tasks = []
completed_tasks = []
deleted_tasks = []

def show_menu():
    """ Creates a Task Tracker menu, displaying the user 
        the title and available menu options to select."""
    print("\nTask Tracker")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Tasks")
    print("5. More Details")
    print("6. Exit")

def add_task():
    """ Function allows users to enter a task into 
        a list of dictionaries if not empty.
        If task entered is empty the function will 
        prompt user that task cannot be empty."""
    
    task_name = input("Enter task: ")

    if task_name.strip() == "":            #Checks if user input was empty. If empty prints appropriate message. 
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
        input("Press Enter to return...")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task["complete"] else "Active"
        print(f"{index}. {task['name']} - {status}")


def delete_tasks():
    """ This function displays a users current task list. 
    If the list is empty function will inform user that it cannot be empty.
    Otherwise function allows user to select task number and delete. 
    Will ask user to confirm decision."""

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        task_index = task_number - 1

        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return

        confirm = input("Are you sure you would like to delete this task? Type yes to confirm: ")

        if confirm.lower() == "yes":
            tasks.pop(task_index)
            print("Task successfully deleted.")
        else:
            print("Action cancelled.")

    except ValueError:
        print("Please enter a valid number.")
        
def mark_complete():
    """ This function marks user selected tasks as complete."""
    view_tasks()

    #Stops action if task list is empty.
    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to mark complete: "))
        task_index = task_number - 1

        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return
        # Asks user for confirmation before fully deleting a task.
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
            delete_tasks()
        elif choice == "5":
            more_details()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


main()
