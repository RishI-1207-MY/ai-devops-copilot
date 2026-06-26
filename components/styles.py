import streamlit as st

def load_css():

    st.markdown("""
<style>

/* ===========================
    Main App
=========================== */

.stApp{

background:#0f172a;

color:white;

}

/* ===========================
    Header
=========================== */

h1{

font-size:40px;

font-weight:800;

color:white;

}

h2,h3{

color:white;

}

/* ===========================
    Sidebar
=========================== */

[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid #334155;

}

[data-testid="stSidebar"] *{

color:white;

}

/* ===========================
    Cards
=========================== */

[data-testid="metric-container"]{

background:linear-gradient(
135deg,
#1e293b,
#111827
);

padding:20px;

border-radius:20px;

border:1px solid #334155;

box-shadow:
0 8px 30px rgba(0,0,0,.35);

transition:.3s;

}

[data-testid="metric-container"]:hover{

transform:translateY(-5px);

}

/* ===========================
    Buttons
=========================== */

.stButton button{

width:100%;

height:50px;

border-radius:15px;

background:#2563eb;

color:white;

font-size:16px;

font-weight:bold;

border:none;

}

.stButton button:hover{

background:#1d4ed8;

}

/* ===========================
    Dataframe
=========================== */

[data-testid="stDataFrame"]{

border-radius:15px;

overflow:hidden;

}

/* ===========================
    Chat
=========================== */

[data-testid="stChatMessage"]{

background:#1e293b;

border-radius:15px;

padding:15px;

margin-bottom:10px;

}

/* ===========================
    File Uploader
=========================== */

[data-testid="stFileUploader"]{

border:2px dashed #3b82f6;

border-radius:15px;

padding:15px;

}

/* ===========================
    Progress
=========================== */

.stProgress > div > div{

background:#22c55e;

}

/* ===========================
    Code
=========================== */

pre{

border-radius:15px;

}

/* ===========================
    Footer
=========================== */

footer{

visibility:hidden;

}

</style>
""",
unsafe_allow_html=True)