import streamlit as st
from components.api import post
from components.loading import ai_loading
from components.ai_report import render_report

st.set_page_config(
    page_title="AI Log Analyzer",
    page_icon="📂",
    layout="wide"
)

st.title("📂 AI Log Analyzer")
st.caption(
    "Upload application logs and let AI automatically detect incidents."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Log File",
    type=["txt", "log", "json"]
)

if uploaded_file is not None:

    st.success(f"Loaded: {uploaded_file.name}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Filename",
            uploaded_file.name
        )

    with col2:
        st.metric(
            "Size",
            f"{round(uploaded_file.size/1024,2)} KB"
        )

    with col3:
        st.metric(
            "Type",
            uploaded_file.type
        )

    st.divider()

    if st.button(
        "🚀 Analyze Logs",
        use_container_width=True
    ):

        ai_loading()

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        response = post(
            "analyze-log",
            files=files
        )

        if response.status_code != 200:

            st.error(
                f"Backend Error ({response.status_code})"
            )

            st.stop()

        result = response.json()

        st.success("Analysis Completed")

        summary = result.get(
            "summary",
            {}
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Lines",
            summary.get("total_lines", 0)
        )

        c2.metric(
            "Errors",
            summary.get("errors", 0)
        )

        c3.metric(
            "Warnings",
            summary.get("warnings", 0)
        )

        c4.metric(
            "Infos",
            summary.get("infos", 0)
        )

        st.divider()

        render_report(
            result.get(
                "ai_report",
                ""
            )
        )

        st.divider()

        left, right = st.columns(2)

        with left:

            st.subheader("🚨 Error Logs")

            errors = result.get(
                "error_logs",
                []
            )

            if errors:

                for err in errors:

                    st.code(
                        err,
                        language="text"
                    )

            else:

                st.success("No Errors Found")

        with right:

            st.subheader("⚠ Warning Logs")

            warnings = result.get(
                "warning_logs",
                []
            )

            if warnings:

                for warn in warnings:

                    st.code(
                        warn,
                        language="text"
                    )

            else:

                st.success("No Warnings Found")

        st.divider()

        st.download_button(
            "⬇ Download AI Report",
            result.get(
                "ai_report",
                ""
            ),
            file_name="incident_report.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.divider()

        st.subheader("💬 Ask AI About This Log")

        question = st.text_input(
            "Ask a question"
        )

        if question:

            ask_response = post(
                "ask",
                json={
                    "question": question
                }
            )

            if ask_response.status_code == 200:

                answer = ask_response.json()

                st.success("Answer")

                st.write(answer)

            else:

                st.error("Unable to contact AI")