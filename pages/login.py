import streamlit as st
from utils.auth import login

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🤖 AI DevOps Copilot")

st.subheader("Administrator Login")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button(
    "Login",
    use_container_width=True
):

    if login(username, password):

        st.session_state.logged_in = True

        st.success("Login Successful")

        st.switch_page("frontend.py")

    else:

        st.error("Invalid Credentials")