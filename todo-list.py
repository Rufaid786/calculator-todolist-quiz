todo_list=[]

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    todo_list.remove(task)    


def print_task():
    print("To Do List:")
    for task in todo_list:
        print(task)    

add_task("Learn python at 5 PM")      
add_task("Take a walk")
# remove_task("Take a walk")
print_task()  
