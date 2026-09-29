from phase2.technical_seo.performance import check_performance


def test_performance():
    result = check_performance("https://example.com")

    assert "status_code" in result
    assert "response_time" in result