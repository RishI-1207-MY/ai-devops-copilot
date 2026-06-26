import streamlit as st
import time

def ai_loading():

    progress = st.progress(0)

    msg = st.empty()

    stages = [

        "Uploading log...",

        "Reading content...",

        "Creating embeddings...",

        "Searching incidents...",

        "Contacting Groq...",

        "Generating report...",

        "Saving incident..."
    ]

    for i, text in enumerate(stages):

        msg.info(text)

        progress.progress(
            (i+1)*14
        )

        time.sleep(.3)

    msg.success("Done")