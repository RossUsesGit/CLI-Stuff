# Let's make a simple to-do list as my first project in Python.
# Made by Rew

print("==========")
print("To-do List App")
print("==========\n")

print("[1] Check current tasks")
print("[2] Add tasks")
print("[3] Delete tasks")

# Load existing tasks from file
tasks = []
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    pass  # No file yet, start with empty list

while True:
    try: 
        function = int(input("\nPlease enter the function you want to use [-1 to exit]: "))

        if not (function in [-1, 143] or 1 <= function <= 3):
            print("\nYou silly! That's not a function.")
            continue

    except ValueError:
        print("\nI'm sure that's not a function, functions are numbers!")
        continue

    # Display tasks
    if function == 1:
        if not tasks:
            print("\nYou don't have any tasks! :3")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}: {task}")

    # Add a task
    elif function == 2:
        new_task = input("\nPlease type out the task you need to do: ")
        tasks.append(new_task)
        print("\nTask added! Updated list:")
        for i, task in enumerate(tasks):
            print(f"{i+1}: {task}")
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

    # Delete a task
    elif function == 3:
        if not tasks:
            print("\nYou don't have any tasks! :3")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}: {task}")
            try:
                remove_input = int(input("\nEnter the number of the task to remove: "))
                index = remove_input - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"\nRemoved task: {removed}")
                    with open("tasks.txt", "w") as file:
                        for task in tasks:
                            file.write(task + "\n")
                    if not tasks:
                        print("\nNo more items left! :3")
                    else:
                        for i, task in enumerate(tasks):
                            print(f"{i+1}: {task}")
                else:
                    print("Invalid number. That task doesn't exist.")
            except ValueError:
                print("Invalid. Please enter a number, bro!")

    elif function == 143:
        print("\nI love you baby Iris. :3")

    elif function == -1:
        print("\nThank you for using Rew's To-Do App. Bye!")
        break
