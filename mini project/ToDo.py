import os

TODO_FILE = "todos.txt"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todos = file.readlines()
        return [todo.strip() for todo in todos]
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")

def show_todos(todos):
    if not todos:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")

def add_todo():
    new_todo = input("Enter a new to-do: ").strip()
    if new_todo:
        todos.append(new_todo)
        save_todos(todos)
        print(f"'{new_todo}' has been added to your to-do list.")
    else:
        print("To-do cannot be empty.")

def remove_todo():
    show_todos(todos)
    try:
        index = int(input("Enter the number of the to-do to remove: ")) - 1
        if 0 <= index < len(todos):
            removed_todo = todos.pop(index)
            save_todos(todos)
            print(f"'{removed_todo}' has been removed from your to-do list.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. View To-Do List")
        print("2. Add To-Do")
        print("3. Remove To-Do")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo()
        elif choice == "3":
            remove_todo()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    todos = load_todos()
    main()