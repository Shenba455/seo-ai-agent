from phase2.technical_seo.robots import check_robots
from phase2.technical_seo.sitemap import check_sitemap
from phase2.technical_seo.https import check_https
from phase2.technical_seo.canonical import check_canonical
from phase2.technical_seo.broken_links import check_link
from phase2.technical_seo.performance import check_performance
from phase2.technical_seo.mobile import check_mobile
from phase2.utils.http_utils import get_page
from phase2.technical_seo.status_codes import check_status_code

def run_technical_audit(url):
    response = get_page(url)

    if response is None:
        return {"error": "Unable to access website"}

    html = response.text

    return {
        "robots": check_robots(url),
        "sitemap": check_sitemap(url),
        "https": check_https(url),
        "canonical": check_canonical(html),
        "status_code": check_status_code(url),
        "broken_link": check_link(url),
        "performance": check_performance(url),
        "mobile": check_mobile(html)
    }