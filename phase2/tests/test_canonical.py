from phase2.technical_seo.canonical import check_canonical


def test_canonical():
    html = '<link rel="canonical" href="https://example.com/">'

    result = check_canonical(html)

    assert result["status"] == "Pass"


def test_missing_canonical():
    html = "<html><head></head></html>"

    result = check_canonical(html)

    assert result["status"] == "Fail"


def test_multiple_canonical():
    html = """
    <link rel="canonical" href="https://example.com/">
    <link rel="canonical" href="https://example.com/page">
    """

    result = check_canonical(html)

    assert result["status"] == "Fail"