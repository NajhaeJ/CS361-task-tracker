#------------------------------------------------------
# Global Lists
#------------------------------------------------------
tasks = []
completed_tasks = []
deleted_tasks = []

#------------------------------------------------------
# Global constants
#------------------------------------------------------

priority_rank = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

#------------------------------------------------------
# Menu Display Helper Functions
#------------------------------------------------------

def show_menu():
    """ Creates a Task Tracker menu, displaying the user
        the title and available menu options to select."""
    print("\nTask Tracker")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Tasks")
    print("5. Edit Tasks")
    print("6. Sort Tasks")
    print("7. More Details")
    print("8. Exit")


def show_view_tasks_menu():
    """ This function displays a
        submenu for users to select what types
        of tasks to view: Completed, Incomplete/Active,
        deleted, more details, and exit."""

    print("\nTask Viewer")
    print("1. All Tasks")
    print("2. Active Tasks")
    print("3. Completed Tasks")
    print("4. Deleted Tasks")
    print("5. More Details")
    print("6. Return to main menu")


def show_sort_tasks_menu():
    """ This functions displays a menu allowing
        users to choose how to sort task lists."""

    print("\nTask Sorting Options")
    print("1. Sort by A-Z")
    print("2. Sort by Z-A")
    print("3. Sort by Due Date")
    print("4. Sort by Priority")
    print("5. Return to main menu")

def show_edit_tasks_menu():
    """ This functions displays a menu of edit task options."""
    print("\nEdit Options")
    print("1. Edit Task Name")
    print("2. Edit Task Description")
    print("3. Edit Task due date")
    print("4. Edit Task priority")
    print("5. Return to main menu")
#------------------------------------------------------
# Task Display Helper Functions
#------------------------------------------------------

def view_active_tasks():
    """ This function displays a users current task list.
    If the list is empty function will inform user that it cannot be empty."""

    if len(tasks) == 0:             #Checks current task list. If list is empty prints "No tasks yet".
        print("No tasks yet.")
        input("Press Enter to return...")
        return

    print("\nYour Active Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Active"
        print(f"{index}. {task['name']} - {status}")


def view_completed_tasks():
    if len(completed_tasks) == 0:             #Checks current task list. If list is empty prints "No tasks yet".
        print("No tasks yet.")
        input("Press Enter to return...")
        return

    print("\nYour Completed Tasks:")
    for index, task in enumerate(completed_tasks, start=1):
        status = "Complete"
        print(f"{index}. {task['name']} - {status}")

def view_deleted_tasks():
    if len(deleted_tasks) == 0:             #Checks current task list. If list is empty prints "No tasks yet".
        print("No tasks yet.")
        input("Press Enter to return...")
        return

    print("\nYour Deleted Tasks:")
    for index, task in enumerate(deleted_tasks, start=1):
        status = "Deleted"
        print(f"{index}. {task['name']} - {status}")

def view_all_tasks():
    if len(tasks) == 0:             #Checks current task list. If list is empty prints "No active tasks yet".
        print("No active tasks yet.")
    # -----------------------------------------------
    # Display active tasks
    # ----------------------------------------------
    print("\nYour Active Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Active"
        print(f"{index}. {task['name']} - {status}")

    #-----------------------------------------------
    # Display completed tasks
    # ----------------------------------------------
    print("\nYour Completed Tasks:")

    if len(completed_tasks) == 0:             #Checks current task list. If list is empty prints "No tasks yet".
        print("No completed tasks yet.")

    for index, task in enumerate(completed_tasks, start=1):
        status = "Complete"
        print(f"{index}. {task['name']} - {status}")

    # -----------------------------------------------
    # Display deleted tasks
    # ----------------------------------------------
    print("\nYour Deleted Tasks:")

    if len(deleted_tasks) == 0:             #Checks current task list. If list is empty prints "No tasks yet".
        print("No deleted tasks yet.")

    for index, task in enumerate(deleted_tasks, start=1):
        status = "Deleted"
        print(f"{index}. {task['name']} - {status}")
#------------------------------------------------------
# Main Task Action Functions
#------------------------------------------------------

def add_task():
    """ Function allows users to enter a task into
        a list of dictionaries if not empty.
        If task entered is empty the function will
        prompt user that task cannot be empty."""

    task_name = input("Enter task: ")  # Cannot be null
    task_description = input("Enter task description: ")  # Can be null
    task_due_date = input("Enter task due date (YYYY-MM-DD): ")  # Cannot be null
    task_priority = input("Enter task priority (High, Medium, Low): ")  # Cannot be null

    if task_name.strip() == "":  # Checks if user input was empty. If empty prints appropriate message.
        print("Task cannot be empty.")
        return

    if task_due_date.strip() == "":
        print("Task due date cannot be empty.")
        return
    if len(task_due_date) != 10 or task_due_date[4] != "-" or task_due_date[7] != "-":
        print("Task due date must be in YYYY-MM-DD format.")
        return

    if task_priority.strip() == "":
        print("Task priority cannot be empty.")
        return
    if task_priority not in ["High", "Medium", "Low"]:
        print("Priority must be one of 'High', 'Medium' or 'Low'.")
        return

    # Creates a task dictionary to be stored in the tasks list.
    task = {
        "name": task_name,
        "description": task_description,
        "due date": task_due_date,
        "priority": task_priority,
        "complete": False
    }

    # Adds task entered to tasks list.
    tasks.append(task)
    print("Task added successfully.")


def mark_complete():
    """ This function marks user selected tasks as complete."""
    view_active_tasks()

    # Stops action if task list is empty.
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
            tasks_completed = tasks[task_index]
            tasks[task_index]["complete"] = True
            completed_tasks.append(tasks_completed)
            tasks.pop(task_index)
            print("Task marked complete.")
        else:
            print("Action cancelled.")

    except ValueError:
        print("Please enter a valid number.")


def delete_tasks():
    """ This function displays a users current task list.
    If the list is empty function will inform user that it cannot be empty.
    Otherwise, function allows user to select task number and delete.
    Will ask user to confirm decision."""

    view_active_tasks()

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
            task_deleted = tasks[task_index]
            deleted_tasks.append(task_deleted)
            tasks.pop(task_index)
            print("Task successfully deleted.")
        else:
            print("Action cancelled.")


    except ValueError:
        print("Please enter a valid number.")


def edit_task():
    """ This function allows the user to edit tasks they've added.
        Allows customer to edit name of task, task description,
        due date and priority."""

    view_active_tasks()

    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter task number to edit: "))
        task_index = task_number - 1

        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return
        else:
            selected_task = tasks[task_index]

            show_edit_tasks_menu()  #Prints edit task menu using helper function

            menu_option = input("Enter menu number to select: ")

            if menu_option == "1": #Ask user for new task name, overrides old task name.
                new_name = input("Enter new task name: ")

                if new_name.strip() == "":  # Checks if user input was empty. If empty prints appropriate message.
                    print("Task cannot be empty.")
                    return
                else:
                    selected_task["name"] = new_name

            elif menu_option == "2": #Ask user for new task description, overrides old description.
                new_description = input("Enter new task description: ")
                selected_task["description"] = new_description

            elif menu_option == "3": #Ask user for new due date, overrides old due date.
                new_due_date = input("Enter new task due date: ")

                #Validate that new due date is not empty
                if new_due_date.strip() == "":
                    print("Task due date cannot be empty.")
                    return
                if len(new_due_date) != 10 or new_due_date[4] != "-" or new_due_date[7] != "-":
                    print("Task due date must be in YYYY-MM-DD format.")
                    return
                else:
                    selected_task["due date"] = new_due_date

            elif menu_option == "4": #Ask user for new priority rating, overrides old priority.
                new_priority = input("Enter new task priority: ")

                #Validates that new priority input is not empty and uses correct ranking.
                if new_priority.strip() == "":
                    print("Task priority cannot be empty.")
                    return
                if new_priority not in ["High", "Medium", "Low"]:
                    print("Priority must be one of 'High', 'Medium' or 'Low'.")
                    return
                selected_task["priority"] = new_priority

            elif menu_option == "5": #Brings user back to main menu.
                return

            else:
                print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")


def sort_tasks():
    """ This functions displays the sort task menu.
        Asks user to choose menu option.
        Implements option user choose."""

    show_sort_tasks_menu()
    try:
        sort_option = int(input("Enter sort option: "))
        if sort_option == 1:
                #Sort A-Z
            if len(tasks) == 0:
                print("No tasks yet to sort.")
                input("Press Enter to return to the main menu.")
                return
            else:
                #If tasks list is not empty, sort tasks list by the dictionary "name" value.
                tasks.sort(key=lambda x: x["name"])
                print("\nTasks sorted successfully!")
                view_active_tasks()

        elif sort_option == 2:
            #Sort Z-A
            if len(tasks) == 0:
                print("No tasks yet to sort.")
                input("Press Enter to return to the main menu.")
                return

            else:
                #If tasks list list is not empty. Sort by names in reverse order.
                tasks.sort(key=lambda x: x["name"], reverse=True)
                print("\nTasks sorted successfully!")
                view_active_tasks()

        elif sort_option == 3:
            #Sort Due Date
            if len(tasks) == 0:
                print("No tasks yet to sort.")
                input("Press Enter to return to the main menu.")
                return
            else:
                #Sorts by due date if tasks list is not empty
                tasks.sort(key=lambda x: x["due date"])
                print("\nTasks sorted successfully!")
                view_active_tasks()

        elif sort_option == 4:
            #Sort by Priority

            #Checks if tasks list is empty
            if len(tasks) == 0:
                print("No tasks yet to sort.")
                input("Press Enter to return to the main menu.")
                return
            else:
                #sorts by priority
                tasks.sort(key=lambda x: priority_rank[x["priority"]])
                print("\nTasks sorted successfully!")
                view_active_tasks()

        elif sort_option == 5:
            "Returns to main menu"
            return

        else:
            print("Invalid option selected. Please choose an option 1-4.")

    except ValueError:
        print("Please enter a valid number.")

def more_details():
    print("\nMore Details")
    print("This app lets users add tasks, view tasks, mark tasks as complete, delete tasks, edit tasks, and sort tasks.")
    print("Users can avoid extra information by staying on the main menu.")
    print("Users can gather more information by choosing this More Details option.")
    input("Press Enter to return to the main menu.")
    return
#------------------------------------------------------
# Menu Controller Functions
#------------------------------------------------------

def view_tasks_menu():
    """ """
    show_view_tasks_menu()
    try:
        views_menu_option = int(input("Enter menu number to select: "))

        if views_menu_option == 1: #Shows all tasks active, completed, deleted.
            view_all_tasks()
        elif views_menu_option == 2:
            view_active_tasks()
        elif views_menu_option == 3:
            view_completed_tasks()
        elif views_menu_option == 4:
            view_deleted_tasks()
        elif views_menu_option == 5:
            more_details()
        elif views_menu_option == 6:
            return
        else:
            print("Invalid option. Please choose an option 1-6.")

    except ValueError:
        print("Please enter a valid number.")

#------------------------------------------------------
# Main Program Loop
#------------------------------------------------------

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks_menu()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_tasks()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            sort_tasks()
        elif choice == "7":
            more_details()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


main()
