from langchain_ollama import ChatOllama

from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage,
    AIMessage
)

from tools.time_calculator import calculate_time
from tools.priority_analyzer import analyze_priority
from tools.schedule_validator import validate_schedule

from agent.prompts import AGENT_SYSTEM_PROMPT
from agent.planner import create_productivity_plan


def get_agent():
    llm = ChatOllama(
        model="qwen2.5:3b",
        temperature=0
    )

    tools = [
        analyze_priority,
        calculate_time,
        validate_schedule
    ]

    llm_with_tools = llm.bind_tools(tools)

    return llm_with_tools


def execute_tool(tool_call):
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    if tool_name == "analyze_priority":
        return analyze_priority.invoke(tool_args)

    elif tool_name == "calculate_time":
        return calculate_time.invoke(tool_args)

    elif tool_name == "validate_schedule":
        return validate_schedule.invoke(tool_args)

    return "Unknown tool."


def run_agent(user_input, max_iterations=6):
    llm = get_agent()

    messages = [
        SystemMessage(
            content=AGENT_SYSTEM_PROMPT
        ),
        HumanMessage(
            content=user_input
        )
    ]

    for _ in range(max_iterations):
        response = llm.invoke(messages)

        messages.append(response)

        if not response.tool_calls:
            break

        for tool_call in response.tool_calls:
            result = execute_tool(tool_call)

            tool_message = ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )

            messages.append(tool_message)

    else:
        return AIMessage(
            content=(
                "I could not complete the plan "
                "within the allowed steps."
            )
        )

    plan = create_productivity_plan(
        user_input,
        messages
    )

    return plan