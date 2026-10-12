#Project Name - To-Do list

#Adding tasks
def add_task(tasks):
    task = input("Enter the tasks to add:")
    tasks.append(task)
    print("Task Added Successfully")

#Updating tasks
def update_task(tasks):
    old_task = input("Enter the task to be updated:")
    index = tasks.index(old_task)
    new_task = input("Enter updated task:")
    tasks[index]=new_task
    print("Task Updated Successfully")

#Removing tasks
def remove_task(tasks):
    task = input("Enter task you want to remove:")
    tasks.remove(task)
    print("Task Removed Successfully")

#Displaying tasks
def display_task(tasks):
    print("Task are: ", tuple(tasks))

tasks = []

while True:
    print("1. Adding Tasks")
    print("2. Updating Tasks")
    print("3. Removing Tasks")
    print("4. Displaying Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5):"))

    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        update_task(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        display_task(tasks)
    elif choice == 5:
        break
    else:
        print("Invalid choice, Try Again")