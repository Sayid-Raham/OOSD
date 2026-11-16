# Task 2: Replace every second task starting at index 1,
# then insert "audit" immediately after the third element.

tasks = ["done", "pending", "done", "pending", "done", "pending"]

tasks[1::2] = ["completed"] * len(tasks[1::2])
tasks[3:3] = ["audit"]

print("Updated tasks:", tasks)
