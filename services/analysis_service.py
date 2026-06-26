from components.api import post


def analyze_log(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    response = post(
        "analyze-log",
        files=files
    )

    if response.status_code != 200:
        raise Exception(
            f"Backend Error ({response.status_code})"
        )

    return response.json()