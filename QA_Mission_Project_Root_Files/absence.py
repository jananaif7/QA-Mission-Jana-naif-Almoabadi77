"""Absence checking functions for the QA Mission project."""

MAX_ABSENCES = 5


def can_sit_exam(absences: int) -> bool:
    """Return True when absences are within the allowed limit."""
    return absences <= MAX_ABSENCES


def status(absences: int) -> str:
    """Return whether the student is allowed to sit the exam."""
    if can_sit_exam(absences):
        return "Allowed"
    return "Blocked"
