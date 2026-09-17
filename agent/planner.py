from llm.ollama_client import get_structured_llm


def create_productivity_plan(user_input, messages):

    context = ""

    for message in messages:

        if hasattr(message, "content"):

            if message.content:

                context = context + "\n" + str(message.content)

    prompt = f"""
You are an AI Personal Productivity Agent.

Create a professional and useful productivity plan based on the
user's request.

USER REQUEST:

{user_input}

AGENT WORK:

{context}

IMPORTANT:

This is a general productivity agent.

The user's request can be about studying, projects, work,
meetings, personal activities, errands, deadlines, interviews,
assignments, or any other type of task.

Do NOT assume that the request is about studying.

Analyze the user's actual request before creating the plan.

For every task provide:

1. task_name
2. priority
3. reason
4. duration
5. deadline
6. order
7. action

PRIORITY:

Use only:
- High
- Medium
- Low

Priority should be based on:
- deadline
- importance
- urgency
- dependencies between tasks

ORDER:

The order must tell the user what they should actually do first,
second, third, and so on.

ACTION:

Explain briefly what the user should do for that task.

REASON:

Explain why that task has its priority and position.

DURATION:

Use the duration given by the user when available.

Do not invent unnecessary durations.

DEADLINE:

Use the deadline provided by the user.

If there is no deadline, use:
"Not specified"

AVAILABLE TIME:

Calculate or use the available time provided by the user.

If the user does not provide available time, use the information
available in the agent work.

SUMMARY:

Give a short professional summary of the complete plan.

ADVICE:

Give practical advice based on the user's actual situation.

If a deadline is close, tell the user what should be focused on first.

If tasks have different deadlines, prioritize earlier deadlines
when appropriate.

If tasks exceed available time, explain what should be prioritized
and what can be reduced or moved.

Keep the advice positive and practical.

TIPS:

Give 3 to 5 useful tips specifically related to the user's request.

Do not give generic motivational statements.

CONCEPTS TO COVER:

This field is optional and depends on the user's request.

If the user is studying something, list the important concepts,
topics, or areas they should cover.

For example, for a Python request:
- OOP
- Exception Handling
- File Handling

For a project request, this field can contain important areas
to complete or verify.

For a normal non-study request where concepts are not relevant,
return an empty list.

Do not force study concepts into non-study tasks.

Do not create tasks that the user did not request.

Do not invent unnecessary information.

Return only the structured productivity plan.
"""

    return get_structured_llm().invoke(prompt)