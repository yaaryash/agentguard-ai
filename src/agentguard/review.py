
from dataclasses import dataclass


@dataclass
class ReviewInput:
    file_path: str
    diff: str


@dataclass
class ReviewFinding:
    file_path: str
    severity: str
    message: str
    rule_id: str = "AG-GENERAL-001"
    diff_line_number: int | None = None


def validate_review_input(review_input: ReviewInput) -> None:
    """Validate the minimum input required for a code review."""
    if not review_input.file_path.strip():
        raise ValueError("File path cannot be empty.")

    if not review_input.diff.strip():
        raise ValueError("Code diff cannot be empty.")
