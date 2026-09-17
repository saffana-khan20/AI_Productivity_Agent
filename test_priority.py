from tools.priority_analyzer import analyze_priority


tasks = [
    "Study for exam tomorrow",
    "Complete assignment",
    "Organize notes",
    "Work on project"
]


result = analyze_priority(tasks)


print("Task Priorities:")

for task, priority in result.items():
    print(task, "->", priority)