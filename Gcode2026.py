todos = []

while True:
    print("\n--- TODO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        todos.append(task)
        print("Task added!")

    elif choice == "2":
        if not todos:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not todos:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")

            number = int(input("Enter the task number to remove: "))

            if 1 <= number <= len(todos):
                removed = todos.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
