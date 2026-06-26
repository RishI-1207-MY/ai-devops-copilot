import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os
from datetime import datetime
from services.monitoring_service import (
    backend_online
)

st.set_page_config(
    page_title="Monitoring",
    page_icon="📈",
    layout="wide"
)

BACKEND = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)

st.title("📈 Monitoring Dashboard")
st.caption("Live backend monitoring powered by Prometheus")

# -------------------------------------------------
# Backend Status
# -------------------------------------------------

try:
    health = requests.get(f"{BACKEND}/", timeout=5)

    if health.status_code == 200:
        backend_online = True
    else:
        backend_online = False

except:
    backend_online = False

# -------------------------------------------------
# Status Cards
# -------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    if backend_online:
        st.success("🟢 Backend Online")
    else:
        st.error("🔴 Backend Offline")

with col2:

    st.metric(
        "Current Time",
        datetime.now().strftime("%H:%M:%S")
    )

with col3:

    st.metric(
        "Environment",
        "AWS EC2"
    )

st.divider()

# -------------------------------------------------
# Incident Summary
# -------------------------------------------------

try:

    history = requests.get(
        f"{BACKEND}/history"
    ).json()

    df = pd.DataFrame(
        history,
        columns=[
            "ID",
            "Filename",
            "Severity",
            "Report",
            "Source",
            "Timestamp"
        ]
    )

    critical = len(df[df["Severity"]=="CRITICAL"])
    high = len(df[df["Severity"]=="HIGH"])
    medium = len(df[df["Severity"]=="MEDIUM"])
    low = len(df[df["Severity"]=="LOW"])

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Total Logs",len(df))
    c2.metric("Critical",critical)
    c3.metric("High",high)
    c4.metric("Medium",medium)
    c5.metric("Low",low)

except:

    st.warning("Unable to fetch incident history.")

st.divider()

# -------------------------------------------------
# Prometheus Metrics
# -------------------------------------------------

st.subheader("📊 Prometheus Metrics")

try:

    metrics = requests.get(
        f"{BACKEND}/metrics"
    ).text

    requests_total = 0
    analyses = 0
    errors = 0

    for line in metrics.splitlines():

        if line.startswith("api_requests_total"):

            requests_total = float(
                line.split()[-1]
            )

        elif line.startswith("log_analysis_total"):

            analyses = float(
                line.split()[-1]
            )

        elif line.startswith("detected_errors_total"):

            errors = float(
                line.split()[-1]
            )

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "API Requests",
        int(requests_total)
    )

    c2.metric(
        "Log Analyses",
        int(analyses)
    )

    c3.metric(
        "Detected Errors",
        int(errors)
    )

except Exception:

    st.error(
        "Unable to fetch Prometheus metrics."
    )

st.divider()

# -------------------------------------------------
# Charts
# -------------------------------------------------

try:

    severity = df["Severity"].value_counts()

    left,right = st.columns(2)

    with left:

        fig = px.pie(
            values=severity.values,
            names=severity.index,
            hole=.45,
            title="Severity Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        files = df["Filename"].value_counts()

        fig = px.bar(
            x=files.index,
            y=files.values,
            title="Top Uploaded Files"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

except Exception as e:
    pass

st.divider()

# -------------------------------------------------
# Recent Activity
# -------------------------------------------------

st.subheader("📝 Latest Incidents")

try:

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )

except Exception as e:

    st.info(
        "No incidents available."
    )

st.divider()

# -------------------------------------------------
# Quick Links
# -------------------------------------------------

st.subheader("🚀 Quick Links")

col1,col2,col3 = st.columns(3)

with col1:

    st.link_button(
        "📄 Swagger Docs",
        f"{BACKEND}/docs",
        use_container_width=True
    )

with col2:

    st.link_button(
        "📈 Prometheus Metrics",
        f"{BACKEND}/metrics",
        use_container_width=True
    )

with col3:

    grafana = st.text_input(
        "Grafana URL",
        placeholder="http://<grafana-ip>:3000"
    )

    if grafana:

        st.link_button(
            "📊 Open Grafana",
            grafana,
            use_container_width=True
        )

st.divider()

st.caption("AI DevOps Copilot Monitoring • FastAPI • Prometheus • AWS • Docker")