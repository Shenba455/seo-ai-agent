def check_https(url):
    if url.startswith("https://"):
        return {
            "status": "Pass",
            "message": "Website is using HTTPS"
        }

    return {
        "status": "Fail",
        "message": "Website is not using HTTPS"
    }