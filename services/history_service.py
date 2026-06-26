from components.api import get
import pandas as pd


COLUMNS = [
    "ID",
    "Filename",
    "Severity",
    "AI Report",
    "Source",
    "Timestamp"
]


def get_history():

    response = get("history")

    if response.status_code != 200:
        raise Exception(
            "Unable to fetch incident history."
        )

    history = response.json()

    return pd.DataFrame(
        history,
        columns=COLUMNS
    )