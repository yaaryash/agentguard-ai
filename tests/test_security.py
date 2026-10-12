
from agentguard.review import ReviewInput
from agentguard.security import scan_security


def test_flags_sql_percent_formatting():
    review_input = ReviewInput(
        file_path="app.py",
        diff="""+cursor.execute("SELECT * FROM users WHERE name = '%s'" % name)""",
    )

    findings = scan_security(review_input)

    assert len(findings) == 1
    assert findings[0].severity == "high"
    assert "SQL injection" in findings[0].message
    assert findings[0].rule_id == "AG-SQL-001"
    assert findings[0].diff_line_number == 1


def test_flags_f_string_execute():
    review_input = ReviewInput(
        file_path="app.py",
        diff="""+cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")""",
    )

    findings = scan_security(review_input)

    assert len(findings) == 1


def test_safe_parameterized_query_is_not_flagged():
    review_input = ReviewInput(
        file_path="app.py",
        diff="""+cursor.execute("SELECT * FROM users WHERE name = %s", (name,))""",
    )

    findings = scan_security(review_input)

    assert findings == []


def test_unrelated_code_is_not_flagged():
    review_input = ReviewInput(
        file_path="app.py",
        diff="+print('hello world')",
    )

    findings = scan_security(review_input)

    assert findings == []
