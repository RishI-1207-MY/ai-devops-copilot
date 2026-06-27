import requests


def backend_alive(url):
    try:
        response = requests.get(url, timeout=2)
        return response.status_code == 200
    except Exception:
        return False


def extract_severity(report: str) -> str:
    """
    Extract severity level from an AI-generated report.
    """

    if not report:
        return "UNKNOWN"

    report = report.lower()

    if "critical" in report:
        return "CRITICAL"

    if "high" in report:
        return "HIGH"

    if "medium" in report:
        return "MEDIUM"

    if "low" in report:
        return "LOW"

    return "INFO"