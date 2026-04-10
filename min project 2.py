
tasks = []



def add_task():
    # Adding a new task to the list [cite: 2185-2187]
    new_task = input("Enter the task description: ")
    tasks.append(new_task)
    print("Task added successfully!")

def remove_task():
    # Removing a task based on its index
    
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter the task number to remove: "))
            if 1 <= task_no <= len(tasks):
                
                removed = tasks.pop(task_no - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            
            print("Error: Please enter a valid number.")

def show_tasks():
    
    print("\n--- Your Current Tasks ---")
    if not tasks:
        print("Your list is empty.")
    else:
    
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def main():
    while True:
        
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ") 
        
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting To-Do Manager. Goodbye!")
            break 
        else:
            print("Invalid choice. Please select 1-4.")


main()