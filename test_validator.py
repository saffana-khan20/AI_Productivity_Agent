from tools.schedule_validator import validate_schedule
from models.task import Task


tasks = [

    Task(
        task_name="Study Python",
        priority="High",
        duration=2,
        deadline="Tomorrow",
        order=1
    ),

    Task(
        task_name="Revise OOP",
        priority="High",
        duration=1.5,
        deadline="Tomorrow",
        order=2
    ),

    Task(
        task_name="Practice programs",
        priority="Medium",
        duration=2,
        deadline="Tomorrow",
        order=3
    )
]


available_hours = 5


result = validate_schedule(tasks, available_hours)


print("Schedule Validation")
print("-------------------")

print("Valid:", result["valid"])
print("Message:", result["message"])
print("Total Time:", result["total_time"], "hours")

if result["valid"] == False:
    print("Extra Time Needed:", result["extra_time"], "hours")