from models.task import Task


task = Task(
    task_name="Study Python",
    priority="High",
    duration=2.0,
    deadline="Tomorrow",
    order=1
)


print("Task Name:", task.task_name)
print("Priority:", task.priority)
print("Duration:", task.duration, "hours")
print("Deadline:", task.deadline)
print("Order:", task.order)