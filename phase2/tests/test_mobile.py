from phase2.technical_seo.mobile import check_mobile


def test_mobile():
    html = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

    result = check_mobile(html)

    assert result["status"] == "Pass"