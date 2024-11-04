#empty list
to_do_list = []

#defining functiona
def add_task(task):
    to_do_list.append(task)

def show_tasks():
    for task in to_do_list:
        print(task)