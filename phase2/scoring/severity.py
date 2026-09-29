def get_severity(score, maximum=100):
    percentage = (score / maximum) * 100

    if percentage < 40:
        return "CRITICAL"
    elif percentage < 60:
        return "HIGH"
    elif percentage < 80:
        return "MEDIUM"
    else:
        return "LOW"