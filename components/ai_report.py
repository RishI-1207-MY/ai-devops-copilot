 # -*- coding: utf-8 -*-
import streamlit as st

def parse_report(report: str):
    data = {
        "Severity": "UNKNOWN",
        "Root Cause": "",
        "Impact": "",
        "Recommendation": ""
    }
    section = None

    for line in report.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("Severity"):
            data["Severity"] = line.split(":", 1)[1].strip()
        elif line.startswith("Root Cause"):
            section = "Root Cause"
        elif line.startswith("Impact"):
            section = "Impact"
        elif line.startswith("Recommendation"):
            section = "Recommendation"
        elif section:
            data[section] += line + "\n"

    return data


def render_report(report: str):
    data = parse_report(report)
    severity = data["Severity"].upper()

    st.subheader("🤖 AI Incident Report")

    if severity == "CRITICAL":
        st.error(f"🚨 Severity : {severity}")
    elif severity == "HIGH":
        st.warning(f"⚠ Severity : {severity}")
    elif severity == "MEDIUM":
        st.info(f"ℹ Severity : {severity}")
    else:
        st.success(f"✅ Severity : {severity}")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 🔍 Root Cause")
        st.info(data["Root Cause"] or "Not Available")

    with c2:
        st.markdown("### ⚠ Impact")
        st.warning(data["Impact"] or "Not Available")

    st.markdown("### ✅ Recommendation")
    st.success(data["Recommendation"] or "Not Available")