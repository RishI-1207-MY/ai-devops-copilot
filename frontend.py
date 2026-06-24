import streamlit as st
import requests
import pandas as pd
import plotly.express as px  # type: ignore[import]
BACKEND_URL = "http://3.106.132.88:8000"
st.set_page_config(
    page_title="AI DevOps Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI DevOps Copilot")
st.subheader("AI-Powered Log Analysis & Incident Detection")
# ================= HISTORY =================

try:
    history = requests.get(f"{BACKEND_URL}/history")

    if history.status_code == 200:
        data = history.json()

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "File",
                "Severity",
                "AI Report",
                "Source",
                "Timestamp"
            ]
        )

        critical_count = len(df[df["Severity"] == "CRITICAL"])
        high_count = len(df[df["Severity"] == "HIGH"])
        medium_count = len(df[df["Severity"] == "MEDIUM"])
        low_count = len(df[df["Severity"] == "LOW"])

        st.divider()
        st.subheader("📊 Dashboard")

        total_analyses = len(df)
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Total Analyses", total_analyses)

        with col2:
            st.metric("🔴 Critical", critical_count)

        with col3:
            st.metric("🟠 High", high_count)

        with col4:
            st.metric("🟡 Medium", medium_count)

        with col5:
            st.metric("🟢 Low", low_count)

        fig = px.histogram(df, x="File", title="Files Analyzed")
        severity_counts = df["Severity"].value_counts()

        fig2 = px.pie(
            values=severity_counts.values,
            names=severity_counts.index,
            title="Incident Severity Distribution"
        )

        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig, use_container_width=True)
        st.divider()

        search = st.text_input("🔍 Search Incident History")
        if search:
            filtered_df = df[
                df["AI Report"]
                .astype(str)
                .str.contains(search, case=False, na=False)
            ]
        else:
            filtered_df = df

        st.subheader("📜 Incident History")
        st.dataframe(filtered_df, use_container_width=True)
        st.download_button(
            label="⬇ Download Incident History",
            data=filtered_df.to_csv(index=False),
            file_name="incident_history.csv",
            mime="text/csv"
        )
        st.divider()

    st.subheader("🧠 AI Incident Summary")
    if st.button("Generate Incident Summary"):
        response = requests.get(f"{BACKEND_URL}/summary")

        if response.status_code == 200:
            result = response.json()
            st.success("Summary Generated")
            st.write(result["summary"])
        else:
            st.error("Failed to generate summary")

except Exception:
    st.error("⚠️ FastAPI backend is not running.")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload Log File",
    type=["txt", "log", "json"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Analyze Logs"):

        with st.spinner("Analyzing logs using AI..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/analyze-log",
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis Complete")

                summary = result.get("summary", {})

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Total Lines",
                        summary.get("total_lines", 0)
                    )

                with col2:
                    st.metric(
                        "Errors",
                        summary.get("errors", 0)
                    )

                with col3:
                    st.metric(
                        "Warnings",
                        summary.get("warnings", 0)
                    )

                with col4:
                    st.metric(
                        "Infos",
                        summary.get("infos", 0)
                    )

                st.divider()

                st.subheader("🧠 AI Analysis")

                ai_report = result.get("ai_report", "")

                st.write(ai_report)
                st.divider()

                st.subheader("🚨 Error Logs")

                for error in result.get("error_logs", []):
                    st.error(error)

                st.subheader("⚠️ Warning Logs")

                for warning in result.get("warning_logs", []):
                    st.warning(warning)

            else:
                st.error(
                    f"Backend Error: {response.status_code}"
                )

    st.subheader(
        "💬 Chat With Logs"
    )

    question = st.text_input(
        "Ask anything about uploaded logs"
    )

    if question:
        response = requests.get(
            f"{BACKEND_URL}/ask",
            params={
                "question": question
            }
        )

        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            try:
                st.json(response.json())
            except Exception:
                st.error("Response is not JSON")
                st.text(response.text)
        else:
            st.error("Backend Error")
            st.text(response.text)
           