import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About AI DevOps Copilot")

st.markdown("""
AI DevOps Copilot is an AI-powered log analysis platform that automates incident detection,
root cause analysis, and troubleshooting recommendations using Large Language Models.

This project demonstrates modern AI + DevOps practices by integrating cloud deployment,
containerization, monitoring, vector search, and Generative AI into a single platform.
""")

st.divider()

# ------------------------------------------------
# Project Features
# ------------------------------------------------

st.header("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✔ AI Powered Log Analysis")
    st.success("✔ Root Cause Detection")
    st.success("✔ Severity Classification")
    st.success("✔ Incident Recommendations")
    st.success("✔ AI Chat with Logs")
    st.success("✔ RAG-based Log Search")

with col2:

    st.success("✔ Docker Deployment")
    st.success("✔ AWS EC2 Hosting")
    st.success("✔ FastAPI Backend")
    st.success("✔ Streamlit Dashboard")
    st.success("✔ Prometheus Metrics")
    st.success("✔ Grafana Ready")

st.divider()

# ------------------------------------------------
# Technology Stack
# ------------------------------------------------

st.header("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.subheader("Frontend")

    st.markdown("""
- Streamlit
- Plotly
- Pandas
- Requests
""")

with tech2:

    st.subheader("Backend")

    st.markdown("""
- FastAPI
- Groq API
- SQLite
- FAISS
- Python
""")

with tech3:

    st.subheader("DevOps")

    st.markdown("""
- Docker
- AWS EC2
- Prometheus
- Grafana
- GitHub Actions (Future)
""")

st.divider()

# ------------------------------------------------
# AI Pipeline
# ------------------------------------------------

st.header("🤖 AI Pipeline")

st.code("""
User Uploads Log
        │
        ▼
 FastAPI Backend
        │
        ▼
 Log Processing
        │
        ▼
 Vector Search (FAISS)
        │
        ▼
 Groq Llama 3.3
        │
        ▼
 AI Incident Report
        │
        ▼
 SQLite Database
        │
        ▼
 Streamlit Dashboard
""")

st.divider()

# ------------------------------------------------
# Deployment Architecture
# ------------------------------------------------

st.header("☁ Deployment Architecture")

st.code("""
                Browser
                   │
                   ▼
        Streamlit Frontend
                   │
        HTTP REST API Calls
                   │
                   ▼
        AWS EC2 Instance
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
   FastAPI Backend       SQLite DB
        │
        ▼
      Groq API
        │
        ▼
 AI Generated Report
        │
        ▼
 Prometheus Metrics
        │
        ▼
     Grafana Dashboard
""")

st.divider()

# ------------------------------------------------
# APIs
# ------------------------------------------------

st.header("🌐 Backend APIs")

st.code("""
GET    /
GET    /docs
GET    /history
GET    /summary
GET    /ask
GET    /metrics

POST   /upload-log
POST   /analyze-log
""")

st.divider()

# ------------------------------------------------
# Folder Structure
# ------------------------------------------------

st.header("📁 Project Structure")

st.code("""
AI DevOps Copilot

├── frontend.py
├── app.py
├── analyzer.py
├── database.py
├── rag/
├── uploads/
├── pages/
│   ├── Dashboard.py
│   ├── Log_Analyzer.py
│   ├── AI_Chat.py
│   ├── Incident_History.py
│   ├── Monitoring.py
│   └── About.py
│
├── components/
│   ├── api.py
│   ├── sidebar.py
│   ├── styles.py
│   ├── metrics.py
│   ├── charts.py
│   └── ai_report.py
""")

st.divider()

# ------------------------------------------------
# Future Improvements
# ------------------------------------------------

st.header("📈 Future Improvements")

st.markdown("""
- Kubernetes Deployment
- CI/CD using GitHub Actions
- JWT Authentication
- Multi-user Support
- Email & Slack Alerts
- Real-time WebSocket Monitoring
- CloudWatch Integration
- OpenTelemetry Support
- LLM Memory
- Multi-LLM Support
""")

st.divider()

# ------------------------------------------------
# Developer
# ------------------------------------------------

st.header("👨‍💻 Developer")

st.info("""
**AI DevOps Copilot**

Developed as an AI + Cloud + DevOps portfolio project demonstrating:

• Generative AI
• FastAPI
• Streamlit
• Docker
• AWS
• Prometheus
• Grafana
• RAG
• Groq LLM Integration
""")

st.caption("Version 2.0 • AI DevOps Copilot")