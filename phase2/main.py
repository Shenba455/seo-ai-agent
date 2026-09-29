from phase2.technical_audit import run_technical_audit
from phase2.scoring.scorer import calculate_technical_score
from phase2.scoring.severity import get_severity
url = input("Enter website URL: ")

result = run_technical_audit(url)

print("\nTechnical SEO Audit")
print("-------------------")

for check, data in result.items():
    print(f"\n{check.upper()}:")
    print(data)

print("\nSEO Score")
print("---------")

technical_score = calculate_technical_score(result)

severity = get_severity(technical_score, 20)

print({
    "technical_seo_score": technical_score,
    "maximum": 20,
    "severity": severity
})