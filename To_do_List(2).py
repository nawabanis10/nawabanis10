import json
task=[]

def load_task():
    global task
    try:

        with open("task.json",'r')as f:
            task=json.load(f)
    except FileNotFoundError:
        task=[]

def save_task():
    with open("task.json","w")as f:
        json.dump(task,f)

def add_task():
    task_title=input("enter your task title: ")
    task.append({'title':task_title,'status':"incomplete"})
    print("task succesfuly add")

def show_task():
    if len(task) == 0:
        print("no task is avilable")
    else:
        for i,t in enumerate (task,start=1):
            print(f"{i}.{t['title']} [{t['status']}]")

def delete_task():
    if len(task) == 0:
        print("no task is avilable")
    else:
        show_task()
    
        index=int(input("enter your task number to delete: "))
        if 1 <= index <= len(task):
            removed=task.pop(index-1)
            print(f"deleted {removed['title']}")
            
        else:
            print("invalid number")

def mark_completed():
    if len(task) == 0:
        print("no task is avilable")
    
    else:
        show_task()
        index=int(input("enter task number to complete:"))
        if 1 <= index <= len(task):
            task[index - 1]['status']="completed"
            print("task marked as completed")
        
        else:
            print("invalid number")

 
def main():
    load_task()

    while True:
        print("\n--- Main Menu ---")

        print("1.add task")
        print("2.show task")
        print("3.delete task")
        print("4.mark task")
        print("5.exit task")

        choice=input("Enter your choice: ")

        if choice == '1':
            add_task()

        elif choice == '2':
            show_task()

        elif choice == '3':
            delete_task()

        elif choice == '4':
            mark_completed()

        elif choice == '5':
            save_task()
            print("exit")
            break

        else:
            print("invalid choice")

main()





