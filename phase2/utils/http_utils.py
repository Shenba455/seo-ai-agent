import requests


def get_page(url):
    try:
        response = requests.get(url, timeout=10)
        return response
    except requests.RequestException:
        return None