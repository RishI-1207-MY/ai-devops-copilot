import streamlit as st
from components.api import get

def show_backend_status():

    try:

        response = get("")

        if response.status_code == 200:

            st.success("🟢 Backend Online")

        else:

            st.error("🔴 Backend Offline")

    except:

        st.error("🔴 Backend Offline")