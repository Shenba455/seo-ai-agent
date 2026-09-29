from bs4 import BeautifulSoup


def check_mobile(html):
    soup = BeautifulSoup(html, "html.parser")

    viewport = soup.find("meta", attrs={"name": "viewport"})

    if viewport:
        return {
            "status": "Pass",
            "message": "Mobile viewport is present"
        }

    return {
        "status": "Fail",
        "message": "Mobile viewport is missing"
    }