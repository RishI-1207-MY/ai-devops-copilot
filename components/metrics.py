import streamlit as st


def dashboard_metrics(df):

    critical = len(
        df[df["Severity"] == "CRITICAL"]
    )

    high = len(
        df[df["Severity"] == "HIGH"]
    )

    medium = len(
        df[df["Severity"] == "MEDIUM"]
    )

    low = len(
        df[df["Severity"] == "LOW"]
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Logs", len(df))
    c2.metric("Critical", critical)
    c3.metric("High", high)
    c4.metric("Medium", medium)
    c5.metric("Low", low)