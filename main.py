from todo import add_task, list_tasks, update_first_task

add_task("Initial task by A")
add_task("B: buy groceries")
add_task("A: clean room")
tasks = list_tasks()
update_first_task("A: updated first task")
for t in tasks:
    print(t)