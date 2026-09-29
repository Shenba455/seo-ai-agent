from phase2.scoring.severity import get_severity


def calculate_technical_score(audit):
    score = 20

    if audit["robots"]["status"] != "Found":
        score -= 3

    if audit["sitemap"]["status"] != "Found":
        score -= 3

    if audit["https"]["status"] != "Pass":
        score -= 3

    if audit["canonical"]["status"] != "Pass":
        score -= 3

    if audit["broken_link"]["broken"]:
        score -= 3

    if audit["mobile"]["status"] != "Pass":
        score -= 2

    return max(score, 0)


def calculate_score(technical, on_page, performance, content):
    total = technical + on_page + performance + content

    return {
        "technical_seo": technical,
        "on_page_seo": on_page,
        "performance": performance,
        "content": content,
        "total": total,
        "severity": get_severity(total)
    }