def remove_last_task():
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    with open("tasks.txt", "w") as f:
        f.writelines(lines[:-1])