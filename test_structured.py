from llm.ollama_client import get_llm


llm = get_llm()


prompt = """
Create one task for a student.

Task:
Study Python OOP

Priority:
High

Available time:
2 hours

Deadline:
Tomorrow
"""


task = llm.invoke(prompt)


print("Task Name:", task.task_name)
print("Priority:", task.priority)
print("Duration:", task.duration, "hours")
print("Deadline:", task.deadline)
print("Order:", task.order)