# Lab 5: Static Code Analysis - Blood Donation Management System
SRN: PES1UG24AM267


## submission note
The complete solution for this lab is located in the **`AM267_Lab5`** folder. 
That folder has the final Python source code, the baseline/final static analysis reports, and the required markdown documentation.

## about the program
This project is a donor register for a blood bank. The original script registers donors after an age check, determines eligibility for subsequent donations (based on a 90-day gap), records donations into a blood-group stock, and calculates how many compatible units are available for a patient.

The original code functioned correctly but contained several quality, style, and security issues of the kind that Pylint, Flake8, and Bandit are built to find.

## work completed
I used three industry-standard static analysis tools to audit and clean the source code. The fixes were split into three separate commits to isolate the changes made for each tool:

*   **Bandit (Security):** Removed a hardcoded password (`B105`), eliminated an insecure `os.system` call (`B605`), replaced the deprecated `tempfile.mktemp` with `tempfile.mkstemp` (`B306`), and replaced an `assert` statement with explicit validation (`B101`).
*   **Pylint (Quality):** Added missing module and function docstrings (`C0114`, `C0116`), converted camelCase functions and variables to snake_case (`C0103`), fixed a mutable default argument (`W0102`), and narrowed a broad exception catch (`W0718`).
*   **Flake8 (PEP 8 Style):** Fixed line lengths (`E501`), removed extra blank lines (`E303`), and corrected whitespace and inline comment formatting (`E261`, `E225`).

## final results
After implementing the fixes, the script was re-evaluated to ensure functionality remained intact and all issues were resolved:
*   **Pylint Score:** `10.00/10`
*   **Bandit:** `No issues identified.`
*   **Flake8:** `0 issues`

## directory structure
*   `blood_donation.py` - The cleaned and updated Python source file
*   `issues.md` - The documented table of identified issues and how they were addressed
*   `reflection.md` - Answers to the reflection questions
*   `reports/before/` - The original analysis reports showing the initial errors
*   `reports/after/` - The final analysis reports showing the clean code
