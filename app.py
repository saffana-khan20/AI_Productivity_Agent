import streamlit as st

from agent.agent import run_agent


st.set_page_config(
    page_title="AI Productivity Agent",
    page_icon="",
    layout="centered"
)


st.markdown(
    """
    <style>

    .stApp {
        background-color: #eef7ff;
    }

    .main-title {
        text-align: center;
        color: #1f4e79;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #555555;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<h1 class="main-title">AI Productivity Agent</h1>',
    unsafe_allow_html=True
)


st.markdown(
    '<p class="subtitle">'
    'Organize your tasks, manage your time, and decide what to do first.'
    '</p>',
    unsafe_allow_html=True
)


st.info(
    "Welcome! Tell me what you need to complete. "
    "You can describe your tasks naturally, including deadlines "
    "and available time."
)


if "messages" not in st.session_state:
    st.session_state.messages = []


if "last_plan" not in st.session_state:
    st.session_state.last_plan = None


def format_duration(hours):

    total_minutes = round(float(hours) * 60)

    if total_minutes < 60:
        return f"{total_minutes} minutes"

    full_hours = total_minutes // 60
    minutes = total_minutes % 60

    if minutes == 0:
        return f"{full_hours} hours"

    return f"{full_hours} hours {minutes} minutes"


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


user_input = st.chat_input(
    "Example: I need to finish my project, attend a meeting, and submit a report by tomorrow."
)


if user_input:

    with st.chat_message("user"):

        st.write(user_input)


    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    with st.chat_message("assistant"):

        with st.spinner("Creating your productivity plan..."):

            try:

                plan = run_agent(user_input)

                st.session_state.last_plan = plan

                st.write(plan.summary)

            except Exception as error:

                st.error(
                    f"Something went wrong: {error}"
                )


    if st.session_state.last_plan:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": st.session_state.last_plan.summary
            }
        )


plan = st.session_state.last_plan


if plan:

    st.divider()

    st.header("Productivity Plan")


    st.subheader("Overview")

    st.write(plan.summary)


    col1, col2, col3 = st.columns(3)


    with col1:

        st.write("**Available Time**")

        st.write(
            format_duration(
                plan.total_available_hours
            )
        )


    with col2:

        st.write("**Planned Time**")

        st.write(
            format_duration(
                plan.total_planned_hours
            )
        )


    with col3:

        st.write("**Schedule**")

        if plan.schedule_valid:

            st.write("Fits available time")

        else:

            st.write("Needs adjustment")


    st.divider()


    st.subheader("What To Do First")


    for task in plan.tasks:

        st.markdown(
            f"### {task.order}. {task.task_name}"
        )

        col1, col2 = st.columns(2)


        with col1:

            st.write(
                f"**Priority:** {task.priority}"
            )

            st.write(
                f"**Duration:** "
                f"{format_duration(task.duration)}"
            )


        with col2:

            st.write(
                f"**Deadline:** {task.deadline}"
            )


        st.write(
            f"**What to do:** {task.action}"
        )

        st.write(
            f"**Why this priority:** {task.reason}"
        )

        st.divider()


    if plan.concepts_to_cover:

        st.subheader("Concepts / Areas To Cover")

        for concept in plan.concepts_to_cover:

            st.write(f"- {concept}")


    st.subheader("Advice")

    st.info(plan.advice)


    st.subheader("Tips")

    for tip in plan.tips:

        st.write(f"- {tip}")


    if not plan.schedule_valid:

        st.warning(
            "Your planned tasks require more time than the "
            "available time. Consider completing the high-priority "
            "tasks first and moving lower-priority tasks."
        )


if st.session_state.messages:

    st.divider()

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.session_state.last_plan = None

        st.rerun()