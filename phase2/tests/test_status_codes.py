from phase2.technical_seo.status_codes import check_status_code


def test_status_code():
    result = check_status_code("https://example.com")

    assert "status_code" in result
    assert "status" in result