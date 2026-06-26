import streamlit as st
from components.styles import load_css
from components.sidebar import sidebar
from components.styles import load_css
from components.sidebar import sidebar
from components.footer import footer

load_css()

sidebar()
st.set_page_config(
    page_title="AI DevOps Copilot",
    page_icon="🤖",
    layout="wide"
)

load_css()

sidebar()

st.markdown("""
# 🤖 AI DevOps Copilot

### AI Powered Incident Detection Platform
""")

st.write(
"""
Analyze logs using **Groq LLM**,
detect production incidents,
monitor deployments,
and chat with your infrastructure.

Built using

- FastAPI
- Streamlit
- Docker
- AWS EC2
- Groq
- Prometheus
- SQLite
"""
)

st.divider()

c1,c2,c3=st.columns(3)

with c1:

    st.metric(
        "Logs Analysed",
        "125"
    )

with c2:

    st.metric(
        "Critical Incidents",
        "18"
    )

with c3:

    st.metric(
        "Backend",
        "🟢 Online"
    )

st.divider()

a,b,c=st.columns(3)

with a:

    if st.button(
        "📂 Analyze Logs",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Log_Analyzer.py"
        )

with b:

    if st.button(
        "📊 Dashboard",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Dashboard.py"
        )

with c:

    if st.button(
        "📈 Monitoring",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Monitoring.py"
        )
        footer()