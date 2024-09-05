# Python program for to_do list
tasks = []

def updatetask():
    task = input("enter a task")
    tasks.append(task)
    print(task,"has been updated to list")

def listtask():
    if tasks==[]:
        print("there is no task ")
    else:
        for index,task in enumerate(tasks):
            print(f"task #{index}.{task}")
def deletetask():
    listtask()
    deletetask=tasks.pop()
    print(deletetask,"is deleted ")



print ("==== Welcome To To-Do List ====")
while True:
    print("\n select one of the choice")
    print("1. Update a task")
    print("2. list task")
    print("3. delete task ")
    print("4. Quit")

    choice = input("enter your choice: ")

    if(choice =="1"):
        updatetask()
    elif(choice == "2"):
        listtask()
    elif(choice =="3"):
        deletetask()
    elif(choice =="4"):
        break
    else:
        print ("invalid input")


