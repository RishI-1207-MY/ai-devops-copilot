from components.footer import footer
from components.metrics import dashboard_metrics
from components.charts import severity_chart, trend_chart
from components.history import incident_table
from components.system_info import system_cards
from services.history_service import get_history
from utils.auth import require_login
from streamlit_autorefresh import st_autorefresh


def load_css():
    pass


def sidebar():
    pass


def backend_status():
    pass

system_cards()

st_autorefresh(

interval=10000,

key="dashboard"

)
require_login()
df = get_history()
load_css()

sidebar()

backend_status()

system_cards()

dashboard_metrics(df)

severity_chart(df)

trend_chart(df)

footer()