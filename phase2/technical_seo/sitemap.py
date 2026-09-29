import requests
import xml.etree.ElementTree as ET


def check_sitemap(url):
    sitemap_url = url.rstrip("/") + "/sitemap.xml"

    try:
        response = requests.get(sitemap_url, timeout=10)

        if response.status_code != 200:
            return {
                "url": sitemap_url,
                "status": "Not Found",
                "urls": []
            }

        urls = []

        try:
            root = ET.fromstring(response.text)

            for element in root.iter():
                if element.tag.endswith("loc"):
                    urls.append(element.text)

        except ET.ParseError:
            return {
                "url": sitemap_url,
                "status": "Invalid",
                "urls": []
            }

        return {
            "url": sitemap_url,
            "status": "Found",
            "urls": urls
        }

    except requests.RequestException as e:
        return {
            "url": sitemap_url,
            "status": "Error",
            "urls": [],
            "error": str(e)
        }