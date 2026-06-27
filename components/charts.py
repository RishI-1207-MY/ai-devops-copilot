import streamlit as st
import plotly.express as px


def severity_chart(df):

    if df.empty:
        st.info("No data available")
        return

    counts = df["Severity"].value_counts()

    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Severity Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
def trend_chart(df):

    if df.empty:
        st.info("No data available")
        return

    if "Timestamp" not in df.columns:
        st.warning("Timestamp column missing")
        return

    fig = px.line(
        df,
        x="Timestamp",
        y="Severity",
        title="Incident Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

def trend_chart(df):

    if df.empty:
        st.info("No data available")
        return

    if "Timestamp" not in df.columns:
        st.warning("Timestamp column missing")
        return

    fig = px.line(
        df,
        x="Timestamp",
        y="Severity",
        title="Incident Trend"
    )

    st.plotly_chart(fig, use_container_width=True)


def file_chart(df):

    if df.empty:
        return

    fig = px.histogram(
        df,
        x="File",
        title="Files Analysed"
    )

    st.plotly_chart(fig, use_container_width=True)