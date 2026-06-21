def extract_severity(report):

    report = report.upper()

    if "CRITICAL" in report:
        return "CRITICAL"

    elif "HIGH" in report:
        return "HIGH"

    elif "MEDIUM" in report:
        return "MEDIUM"

    elif "LOW" in report:
        return "LOW"

    elif "ERROR" in report:
        return "HIGH"

    elif "WARNING" in report:
        return "MEDIUM"

    return "LOW"