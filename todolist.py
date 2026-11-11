#DATA BASE
task_list = []

# Add Tast

def add_task(): 
    task = input("Enter your task: ")
    task_list.append(task)
    print("Task Added !")

# Delete Task

def delete_task():
    view_tasks()
    num_task = int(input("Enter the task number :"))
    removed_task = task_list.pop(num_task - 1)
    print("you have removed :", removed_task )



#View_Task
def view_tasks():
    if len(task_list) == 0:
        print("No Task availible")

    else:
        print("---Your ToDo list--- :\n")
        for i in range(len(task_list)):
            print(str(i+1)+ ")" + task_list[i])

        print()




while True:
    print("Choose an option : [1] Add, [2] Dalete, [3] View, [4] Exit ") 
    choice = int(input("Choice :")) 
    if choice == 4: 
        print("Exit the program.") 
        break

    if choice == 1:
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        view_tasks()
    else:
        print("Your choics out of ( 1 - 2 - 3 - 4 )")       

