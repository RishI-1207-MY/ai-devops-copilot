import streamlit as st

def success(msg):

    st.toast(
        msg,
        icon="✅"
    )

def warning(msg):

    st.toast(
        msg,
        icon="⚠️"
    )

def error(msg):

    st.toast(
        msg,
        icon="❌"
    )