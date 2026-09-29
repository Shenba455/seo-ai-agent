from phase2.scoring.scorer import calculate_score
from phase2.scoring.severity import get_severity

def test_scoring():
    result = calculate_score(18, 30, 16, 18)

    assert result["total"] == 82
    assert result["severity"] == "LOW"
def test_severity():
    assert get_severity(7, 20) == "CRITICAL"
    assert get_severity(11, 20) == "HIGH"
    assert get_severity(14, 20) == "MEDIUM"
    assert get_severity(18, 20) == "LOW"