# QA Mission – RP05 · Unit 4

A small Python project that checks passing grades and exam absence limits.

## Project files

- `grades.py` – checks whether a score is a pass and returns the result.
- `absence.py` – checks whether a student is allowed to sit the exam.
- `test_grades.py` – automated tests for grade rules, including boundary values.
- `test_absence.py` – automated tests for absence rules, including boundary values.
- `requirements.txt` – project test dependency.

## Rules

- A score of **50 or higher** is a pass.
- **5 absences or fewer** means `Allowed`.
- More than **5 absences** means `Blocked`.

## Run the tests in Google Colab

1. Upload the project files to Colab, or clone your GitHub repository.
2. Run:

```python
!pip install pytest
!pytest -q
```

All tests should pass.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
