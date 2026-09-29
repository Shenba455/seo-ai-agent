from phase2.technical_seo.sitemap import check_sitemap


def test_sitemap():
    result = check_sitemap("https://example.com")

    assert "status" in result
    assert "url" in result
    assert "urls" in result