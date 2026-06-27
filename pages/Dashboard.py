from components.footer import footer
from components.metrics import dashboard_metrics
from components.charts import severity_chart, trend_chart
from components.history_table import history_table
from components.system_info import system_cards
from services.history_service import get_history
from utils.auth import require_login
from streamlit_autorefresh import st_autorefresh
from components.sidebar import sidebar
from components.backend_status import show_backend_status

def load_css():
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

show_backend_status()


dashboard_metrics(df)

severity_chart(df)

trend_chart(df)

footer()

history_table(df)