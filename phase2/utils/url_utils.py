from urllib.parse import urljoin


def make_url(base_url, link):
    return urljoin(base_url, link)