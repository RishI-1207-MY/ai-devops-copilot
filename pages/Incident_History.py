import streamlit as st
import pandas as pd
import plotly.express as px
from components.api import get

st.set_page_config(
    page_title="Incident History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Incident History")
st.caption("Browse, filter and export previous AI log analyses.")

# -----------------------------
# Fetch Data
# -----------------------------

try:
    response = get("history")

    if response.status_code != 200:
        st.error("Unable to connect to backend.")
        st.stop()

    history = response.json()

except Exception:
    st.error("Backend Offline")
    st.stop()

# -----------------------------
# DataFrame
# -----------------------------

columns = [
    "ID",
    "Filename",
    "Severity",
    "AI Report",
    "Source",
    "Timestamp"
]

df = pd.DataFrame(history, columns=columns)

if df.empty:
    st.info("No incidents found.")
    st.stop()

# -----------------------------
# Filters
# -----------------------------

st.sidebar.header("Filters")

severity = st.sidebar.multiselect(
    "Severity",
    options=sorted(df["Severity"].unique()),
    default=list(df["Severity"].unique())
)

filename = st.sidebar.text_input("Filename")

keyword = st.sidebar.text_input("Search AI Report")

filtered = df.copy()

filtered = filtered[
    filtered["Severity"].isin(severity)
]

if filename:

    filtered = filtered[
        filtered["Filename"]
        .str.contains(
            filename,
            case=False,
            na=False
        )
    ]

if keyword:

    filtered = filtered[
        filtered["AI Report"]
        .astype(str)
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

# -----------------------------
# Metrics
# -----------------------------

critical = len(
    filtered[
        filtered["Severity"]=="CRITICAL"
    ]
)

high = len(
    filtered[
        filtered["Severity"]=="HIGH"
    ]
)

medium = len(
    filtered[
        filtered["Severity"]=="MEDIUM"
    ]
)

low = len(
    filtered[
        filtered["Severity"]=="LOW"
    ]
)

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("Total",len(filtered))
c2.metric("Critical",critical)
c3.metric("High",high)
c4.metric("Medium",medium)
c5.metric("Low",low)

st.divider()

# -----------------------------
# Charts
# -----------------------------

left,right = st.columns(2)

with left:

    severity_count = (
        filtered["Severity"]
        .value_counts()
    )

    fig = px.pie(
        values=severity_count.values,
        names=severity_count.index,
        hole=.45,
        title="Severity Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    files = (
        filtered["Filename"]
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=files.index,
        y=files.values,
        title="Most Analysed Files"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------------
# Incident Table
# -----------------------------

st.subheader("Incident Table")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# View Incident
# -----------------------------

st.divider()

st.subheader("View Full Incident")

incident = st.selectbox(
    "Choose Incident",
    filtered["ID"]
)

selected = filtered[
    filtered["ID"]==incident
].iloc[0]

st.markdown(
    f"### 📄 {selected['Filename']}"
)

col1,col2,col3 = st.columns(3)

col1.metric(
    "Severity",
    selected["Severity"]
)

col2.metric(
    "Source",
    selected["Source"]
)

col3.metric(
    "Incident ID",
    selected["ID"]
)

st.markdown("### 🤖 AI Report")

st.code(
    selected["AI Report"],
    language="text"
)

# -----------------------------
# Download
# -----------------------------

st.divider()

csv = filtered.to_csv(index=False)

st.download_button(
    "⬇ Download CSV",
    csv,
    "incident_history.csv",
    "text/csv",
    use_container_width=True
)