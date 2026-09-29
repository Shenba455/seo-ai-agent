import requests
import time


def check_performance(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        end = time.time()

        return {
            "url": url,
            "status_code": response.status_code,
            "response_time": round(end - start, 2)
        }

    except requests.RequestException as e:
        return {
            "url": url,
            "status_code": None,
            "response_time": None,
            "error": str(e)
        }