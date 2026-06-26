import streamlit as st


def export_report(report):

    st.download_button(

        "📄 Download TXT",

        report,

        "report.txt"

    )

    st.download_button(

        "📑 Download MD",

        report,

        "report.md"

    )