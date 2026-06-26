 # -*- coding: utf-8 -*-
import streamlit as st
from components.api import get

st.set_page_config(
    page_title="AI Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI DevOps Assistant")
st.caption("Chat with your uploaded logs using Groq AI")

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("💡 Suggested Questions")

    suggestions = [
        "Summarize the uploaded logs",
        "What is the root cause?",
        "List all errors",
        "List all warnings",
        "How can I fix the issue?",
        "Which service failed?",
        "Give deployment recommendations",
        "Is this a critical incident?"
    ]

    for q in suggestions:

        if st.button(q, use_container_width=True):

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": q
                }
            )

    st.divider()

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Chat History
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input(
    "Ask anything about your uploaded logs..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        with st.spinner("🧠 Groq is analysing logs..."):

            try:

                response = get(
                    "ask",
                    params={
                        "question": question
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    answer = result.get(
                        "answer",
                        "No response."
                    )

                    placeholder.markdown(answer)

                    if result.get("retrieved_logs"):

                        with st.expander(
                            "📄 Retrieved Context"
                        ):

                            for i, log in enumerate(
                                result["retrieved_logs"],
                                start=1
                            ):

                                st.code(
                                    log,
                                    language="text"
                                )

                else:

                    answer = (
                        f"Backend Error "
                        f"{response.status_code}"
                    )

                    placeholder.error(answer)

            except Exception as e:

                answer = str(e)

                placeholder.error(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )