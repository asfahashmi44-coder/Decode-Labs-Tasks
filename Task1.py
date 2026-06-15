# =====================================================================
# PART 1: YOUR ORIGINAL TO-DO LIST (Basic List & Append)
# =====================================================================

# Initialize an empty list to store the tasks
todo_list = []

print("--- Welcome to your To-Do List App (Part 1) ---")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Move to Advanced Features")  # Changed from "Exit" to transition smoothly
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        new_task = input("Enter the task: ")
        todo_list.append(new_task)
        print(f"'{new_task}' has been added!")
        
    elif choice == "2":
        print("\nYour Current Tasks:")
        if not todo_list:
            print("[Your list is empty!]")
        else:
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
    elif choice == "3":
        print("\nTransitioning to Advanced Features...")
        break  # This breaks Part 1's loop so Python can move to the code below!
        
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


# =====================================================================
# PART 2: IMPROVED TO-DO LIST (With Update & Delete)
# =====================================================================

# We convert your existing tasks into the new format: [task_name, status]
advanced_todo_list = []
for task in todo_list:
    advanced_todo_list.append([task, "Pending"])

print("\n--- Welcome to your Advanced To-Do List App (Part 2) ---")

while True:
    print("\n" + "="*20)
    print("Options:")
    print("1. Add a new task")
    print("2. View tasks (with Status)")
    print("3. Mark task as Completed")
    print("4. Delete a task")
    print("5. Exit completely")
    print("="*20)
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        new_task = input("Enter the task: ")
        advanced_todo_list.append([new_task, "Pending"])
        print(f"'{new_task}' has been added!")
        
    elif choice == "2":
        print("\nYour Current Tasks:")
        if not advanced_todo_list:
            print("[Your list is empty!]")
        else:
            for index, item in enumerate(advanced_todo_list, start=1):
                print(f"{index}. [{item[1]}] {item[0]}")
                
    elif choice == "3":
        if not advanced_todo_list:
            print("No tasks to update.")
        else:
            print("\nWhich task did you complete?")
            for index, item in enumerate(advanced_todo_list, start=1):
                print(f"{index}. [{item[1]}] {item[0]}")
                
            try:
                task_num = int(input("Enter task number to mark completed: "))
                advanced_todo_list[task_num - 1][1] = "✓ Completed"
                print("Task updated successfully!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        if not advanced_todo_list:
            print("No tasks to delete.")
        else:
            print("\nWhich task do you want to remove?")
            for index, item in enumerate(advanced_todo_list, start=1):
                print(f"{index}. [{item[1]}] {item[0]}")
                
            try:
                task_num = int(input("Enter task number to delete: "))
                removed_task = advanced_todo_list.pop(task_num - 1)
                print(f"Removed: '{removed_task[0]}'")
            except (ValueError, IndexError):
                print("Invalid task number.")
                
    elif choice == "5":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please choose between 1 and 5.")


