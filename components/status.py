import streamlit as st
import requests
import os

BACKEND = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)


def backend_status():

    try:

        requests.get(
            BACKEND,
            timeout=2
        )

        st.success(
            "🟢 Backend Online"
        )

    except:

        st.error(
            "🔴 Backend Offline"
        )