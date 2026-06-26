import streamlit as st
from components.backend_status import show_backend_status
from utils.auth import logout
def sidebar():

    with st.sidebar:

        st.markdown(
        """
        <div style='text-align:center;'>

        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" width="90">

        <h2 style='margin-bottom:0'>
        AI DevOps Copilot
        </h2>

        <p style='color:gray'>
        AI Powered Log Analysis
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )

        st.divider()

        show_backend_status()

        st.divider()

        st.page_link(
            "frontend.py",
            label="🏠 Home"
        )

        st.page_link(
            "pages/Dashboard.py",
            label="📊 Dashboard"
        )

        st.page_link(
            "pages/Log_Analyzer.py",
            label="📂 Log Analyzer"
        )

        st.page_link(
            "pages/AI_Chat.py",
            label="🤖 AI Assistant"
        )

        st.page_link(
            "pages/Incident_History.py",
            label="📜 Incident History"
        )

        st.page_link(
            "pages/Monitoring.py",
            label="📈 Monitoring"
        )

        st.page_link(
            "pages/About.py",
            label="ℹ About"
        )

        st.divider()

        st.markdown(
        """
        ### 🚀 Deployment

        ✔ AWS EC2

        ✔ Docker

        ✔ FastAPI

        ✔ Groq

        ✔ SQLite

        ✔ Prometheus

        ✔ Grafana Ready
        """
        )

        st.divider()

        st.caption("Version 2.0")
        
        st.divider()

if st.button(
    "🚪 Logout",
    use_container_width=True
):

    logout()

    st.switch_page("pages/Login.py")
    st.sidebar.image(

"assets/logo.png",

width=120

)