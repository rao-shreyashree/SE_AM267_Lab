# AM267 Lab 5 - Issues Identified and Fixed

| Issue | Type | Line(s)| Description | Fix Approach |
|---|---|---|---|---|
| B105 hardcoded password | Bandit - High | 5 | `OFFICER_PASSWORD` stores a credential in source code. | Removed the unused constant |
| B605 shell injection | Bandit - High | 65 | `os.system` builds a shell command from input. | Removed the unused insecure helper `notifyDonors()` |
| B306 insecure temp file | Bandit - Medium | 60 | `tempfile.mktemp()` is race-condition prone. | Replaced with `tempfile.mkstemp()` |
| B101 use of assert | Bandit - Low | 18 | `assert` disappears when Python runs with `-O`. | Replaced with explicit `if not ...: raise ValueError` |
| W0102 dangerous default | Pylint - Medium | 17 | `notes=[]` is a mutable default shared across calls. | Changed to `notes=None` and initialize inside |
| W0718 broad exception | Pylint - Medium | 45 | `except Exception:` hides real bugs. | Catch only `KeyError` |
| C0103 invalid name | Pylint - Low | multiple | camelCase names. | Renamed to snake_case |
| C0114 / C0116 docstrings | Pylint - Low | multiple | Missing docstrings. | Added module and function docstrings |
| E501 line too long | Flake8 - Low | 7, 82 | Lines exceeded 79 chars. | Wrapped lines |
| E303 too many blank lines | Flake8 - Low | 58 | 3 blank lines. | Reduced to 2 |
| E261 inline comment | Flake8 - Low | 80 | Missing spaces before comment. | Added 2 spaces before `#` |
| E225 missing whitespace | Flake8 - Low | 81 | `eligible=[...]` | Changed to `eligible = [...]` |