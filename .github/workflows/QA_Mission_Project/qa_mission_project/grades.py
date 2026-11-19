"""Grade checking functions for the QA Mission project."""

PASS_MARK = 50


def is_pass(score: int) -> bool:
    """Return True when the score meets the passing mark."""
    return score >= PASS_MARK


def result(score: int) -> str:
    """Return the student's result as text."""
    if is_pass(score):
        return "Pass"
    return "Fail"
