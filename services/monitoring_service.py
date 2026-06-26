from components.api import get


def backend_online():

    try:

        response = get("")

        return response.status_code == 200

    except:

        return False


def get_metrics():

    response = get("metrics")

    if response.status_code != 200:
        return {}

    metrics = {}

    for line in response.text.splitlines():

        if line.startswith("#"):
            continue

        if " " not in line:
            continue

        key, value = line.split()

        try:
            metrics[key] = float(value)
        except:
            pass

    return metrics