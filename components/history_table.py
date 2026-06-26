import streamlit as st

def history_table(df):

    search = st.text_input(
        "🔍 Search Incident"
    )

    if search:

        df = df[
            df["AI Report"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "⬇ Download CSV",
        df.to_csv(index=False),
        "incident_history.csv",
        "text/csv"
    )