import streamlit as st
import psutil


def system_cards():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "CPU",
        f"{cpu}%"
    )

    c2.metric(
        "RAM",
        f"{ram}%"
    )

    c3.metric(
        "Disk",
        f"{disk}%"
    )