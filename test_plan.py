from llm.ollama_client import get_llm


llm = get_llm()


prompt = """
Create a productivity plan for these tasks:

1. Study Python
   Priority: High
   Duration: 2 hours
   Deadline: Tomorrow

2. Revise OOP
   Priority: Medium
   Duration: 1.5 hours
   Deadline: This week

3. Practice programs
   Priority: Low
   Duration: 1 hour
   Deadline: Next month

Available time: 6 hours

Return the productivity plan.
"""


result = llm.invoke(prompt)


print("\nProductivity Plan:")
print(result)


print("\nTasks:")

for task in result.tasks:

    print(
        task.order,
        task.task_name,
        "->",
        task.priority,
        "->",
        task.duration,
        "hours"
    )


print("\nTotal Available Hours:", result.total_available_hours)
print("Total Planned Hours:", result.total_planned_hours)
print("Schedule Valid:", result.schedule_valid)