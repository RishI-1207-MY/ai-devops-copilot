from components.api import get


def ask_ai(question):

    response = get(
        "ask",
        params={
            "question": question
        }
    )

    if response.status_code != 200:
        raise Exception(
            "Unable to contact backend."
        )

    return response.json()