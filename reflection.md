# AM267 Lab 5 - Reflection

## 1. Purpose of static code analysis and which tool found which kind of issue?

Static analysis checks source code without executing it to find style problems, bugs, and security risks. 
a. Pylint found code-quality issues (mutable default arguments, broad exceptions, invalid names, missing docstrings). 
b. Flake8 found PEP 8 formatting issues (line lengths, spacing, blank lines). 
c. Bandit found security issues (hardcoded password, `os.system` shell command, `assert`, insecure `tempfile.mktemp`).

## 2. Which issues were fixed, and how were they verified?

I fixed all Bandit findings, the Pylint issues, and all Flake8 formatting issues. 
- the hardcoded password and insecure `notifyDonors()` helper were removed. 
- `assert` was replaced with an explicit `ValueError`. `tempfile.mktemp` was replaced with `tempfile.mkstemp`. 
- the mutable default was changed to `None`, the broad exception was narrowed to `KeyError`, names were converted to snake_case, and docstrings were added.

Then I reran all three tools: Bandit reported no issues, Flake8 produced no output, and Pylint scored 10.00/10. The program output remained identical.

## 3. What was the most challenging part?
Deciding how to fix Bandit findings without changing the demo’s behavior. `notifyDonors()` and `OFFICER_PASSWORD` were not used by `main()`, so removing them was the cleanest fix. For `assert`, I replaced it with explicit validation because `assert` can be disabled. For the broad exception, I identified that only `KeyError` was expected from an unknown blood group.

## 4. How does static analysis improve code quality and maintainability?
It catches problems early, before testing or deployment. It makes code more readable and consistent by enforcing style, reduces hidden bugs like shared mutable defaults, and highlights security risks like hardcoded credentials. It provides a repeatable check that can be run after every change, making code easier to maintain and review.