from bs4 import BeautifulSoup


def check_canonical(html):
    soup = BeautifulSoup(html, "html.parser")

    canonicals = soup.find_all("link", rel="canonical")

    if len(canonicals) == 0:
        return {
            "status": "Fail",
            "message": "Canonical tag is missing"
        }

    if len(canonicals) > 1:
        return {
            "status": "Fail",
            "message": "Multiple canonical tags found"
        }

    href = canonicals[0].get("href")

    if not href:
        return {
            "status": "Fail",
            "message": "Canonical tag has no URL"
        }

    return {
        "status": "Pass",
        "message": "Canonical tag is present",
        "url": href
    }