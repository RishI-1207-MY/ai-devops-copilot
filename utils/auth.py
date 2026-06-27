import os
import streamlit as st


def login(username, password):
    admin_user = os.getenv("ADMIN_USERNAME", "admin")
    admin_pass = os.getenv("ADMIN_PASSWORD", "admin123")

    if username == admin_user and password == admin_pass:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        return True

    return False


def logout():
    st.session_state.clear()
    st.switch_page("pages/login.py")


def require_login():
    if not st.session_state.get("logged_in", False):
        st.warning("Please login first.")
        st.switch_page("pages/login.py")