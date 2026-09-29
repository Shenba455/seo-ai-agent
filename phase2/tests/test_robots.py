from phase2.technical_seo.robots import check_robots


def test_robots():
    result = check_robots("https://example.com")

    assert "status" in result
    assert "url" in result

    if result["status"] == "Found":
        assert "disallow" in result