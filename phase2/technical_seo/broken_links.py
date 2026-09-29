import requests


def check_link(url):
    try:
        response = requests.get(url, timeout=10)

        return {
            "url": url,
            "status_code": response.status_code,
            "broken": response.status_code >= 400
        }

    except requests.RequestException:
        return {
            "url": url,
            "status_code": None,
            "broken": True
        }


def check_links(urls):
    results = []

    for url in urls:
        results.append(check_link(url))

    return results