from phase2.technical_seo.https import check_https


def test_https():
    result = check_https("https://example.com")

    assert result["status"] == "Pass"