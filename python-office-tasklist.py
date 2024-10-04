office_tasklist = []  

def add_task():
    task = str(input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll. \n"))
    if task:
       office_tasklist.append(task)
       print(f"The task {task} was added to your list.")
    else:
        print("Your tasklist ist empty.")
add_task()

def show_tasklist():
    if office_tasklist == None:
        print("Your tasklist ist empty.")
    else:
        print("Your tasklist:")
    for task in office_tasklist:
        print(task)
show_tasklist