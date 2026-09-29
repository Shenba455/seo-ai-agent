import requests


def check_robots(url):
    robots_url = url.rstrip("/") + "/robots.txt"

    try:
        response = requests.get(robots_url, timeout=10)

        if response.status_code != 200:
            return {
                "url": robots_url,
                "status": "Not Found",
                "content": ""
            }

        content = response.text

        disallow = []

        for line in content.splitlines():
            line = line.strip()

            if line.lower().startswith("disallow:"):
                path = line.split(":", 1)[1].strip()

                if path:
                    disallow.append(path)

        return {
            "url": robots_url,
            "status": "Found",
            "disallow": disallow,
            "content": content
        }

    except requests.RequestException as e:
        return {
            "url": robots_url,
            "status": "Error",
            "content": str(e)
        }