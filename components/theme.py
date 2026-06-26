import streamlit as st


def theme_toggle() -> bool:
    """Render a dark mode toggle in the sidebar and return its state.

    Returns:
        bool: True if dark mode is enabled, False otherwise.
    """
    dark = st.sidebar.checkbox("🌙 Dark Mode", value=True)
    return bool(dark)