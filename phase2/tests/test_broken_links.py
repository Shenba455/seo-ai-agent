from phase2.technical_seo.broken_links import check_link, check_links


def test_broken_link():
    result = check_link("https://example.com")

    assert "status_code" in result
    assert "broken" in result


def test_multiple_links():
    urls = [
        "https://example.com",
        "https://example.com/about"
    ]

    results = check_links(urls)

    assert len(results) == 2
    assert "url" in results[0]
    assert "broken" in results[0]