
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
    findings: list[ReviewFinding] = []

    for line_number, line in enumerate(review_input.diff.splitlines(), start=1):
        # Ignore removed lines and diff metadata.
        if not line.startswith("+") or line.startswith("+++"):
            continue

        added_code = line[1:]

        if (
            SQL_PERCENT_FORMAT_PATTERN.search(added_code)
            or SQL_FSTRING_PATTERN.search(added_code)
        ):
            findings.append(
                ReviewFinding(
                    file_path=review_input.file_path,
                    severity="high",
                    message=(
                        "Potential SQL injection: SQL execution may use "
                        "string interpolation. Prefer parameterized queries."
                    ),
                    rule_id="AG-SQL-001",
                    diff_line_number=line_number,
                )
            )

    return findings
