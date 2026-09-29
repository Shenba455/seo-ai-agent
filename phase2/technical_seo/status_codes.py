import requests


def check_status_code(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            status = "OK"
        elif response.status_code in [301, 302]:
            status = "Redirect"
        elif response.status_code == 404:
            status = "Not Found"
        elif response.status_code >= 500:
            status = "Server Error"
        else:
            status = "Other"

        return {
            "url": url,
            "status_code": response.status_code,
            "status": status
        }

    except requests.RequestException as e:
        return {
            "url": url,
            "status_code": None,
            "status": "Error",
            "error": str(e)
        }