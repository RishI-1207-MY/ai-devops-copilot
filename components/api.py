import os
import requests

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)


def get(endpoint, **kwargs):

    return requests.get(
        f"{BACKEND_URL}/{endpoint}",
        timeout=60,
        **kwargs
    )


def post(endpoint, **kwargs):

    return requests.post(
        f"{BACKEND_URL}/{endpoint}",
        timeout=120,
        **kwargs
    )