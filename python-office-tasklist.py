office_tasklist = []  

def add_task():
    task = str(input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll. \n"))
    if task:
       office_tasklist.append(task)
       print(f"The task {task} was added to your list.")
    else:
        print("Your tasklist ist empty.")


def show_tasklist():
    if office_tasklist == None:
        print("Your tasklist ist empty.")
    else:
        for task in office_tasklist:
            print("Your tasklist:")
            print(task)
show_tasklist()

def main():
    while True:
        print("1. Add a task")
        print("2. Show the list.")
        print("3. End the programm.")
        choice = input("Please make your choice.")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            print("Good Bye.")
            break


if __name__=="__main__":
    main()