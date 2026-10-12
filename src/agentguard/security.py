
import re

from agentguard.review import ReviewFinding, ReviewInput


SQL_PERCENT_FORMAT_PATTERN = re.compile(
    r"""execute\s*\(\s*["'][^"']*["']\s*%\s*[A-Za-z_(]""",
    re.IGNORECASE,
)

SQL_FSTRING_PATTERN = re.compile(
    r"""execute\s*\(\s*f["']""",
    re.IGNORECASE,
)


def scan_security(review_input: ReviewInput) -> list[ReviewFinding]:
    """Detect selected potentially unsafe SQL string construction patterns."""
    diff = review_input.diff
    findings: list[ReviewFinding] = []

    if SQL_PERCENT_FORMAT_PATTERN.search(diff) or SQL_FSTRING_PATTERN.search(diff):
        findings.append(
            ReviewFinding(
                file_path=review_input.file_path,
                severity="high",
                message=(
                    "Potential SQL injection: SQL execution may use "
                    "string interpolation. Prefer parameterized queries."
                ),
            )
        )

    return findings
