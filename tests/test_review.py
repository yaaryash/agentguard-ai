
import pytest

from agentguard.review import ReviewInput, validate_review_input


def test_valid_review_input():
    review_input = ReviewInput(
        file_path="src/app.py",
        diff="+print('hello')",
    )

    validate_review_input(review_input)


def test_empty_file_path():
    review_input = ReviewInput(
        file_path=" ",
        diff="+print('hello')",
    )

    with pytest.raises(ValueError, match="File path cannot be empty"):
        validate_review_input(review_input)


def test_empty_diff():
    review_input = ReviewInput(
        file_path="src/app.py",
        diff=" ",
    )

    with pytest.raises(ValueError, match="Code diff cannot be empty"):
        validate_review_input(review_input)
