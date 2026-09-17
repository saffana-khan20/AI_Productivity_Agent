from agent.agent import run_agent


user_input = """
I have these tasks:

Study Python - deadline tomorrow
Revise OOP - deadline this week
Practice programs - deadline next month

I have 6 hours available.

First analyze the priority of the tasks.

Then calculate how much time I should spend on each task.

Finally check whether all tasks fit within my available 6 hours.

Give me the final plan in simple terms.
"""


response = run_agent(user_input)

print("\nFinal Agent Response:")
print(response.content)