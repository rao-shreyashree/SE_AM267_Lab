# Lab 6: Code and Branch Coverage - Airline Baggage Fees
SRN: PES1UG24AM267

## submission note
The complete solution for this lab is located in the **`AM267_Lab6`** folder.
That folder has the module under test, two separate coverage test files, and the terminal screenshots of the final coverage reports.

## about the program
`airline_baggage.py` is a small fare-rules module with three functions:

*   `baggage_fee(cabin, weight_kg, route, is_member)` - validates the cabin and weight, applies the free allowance for the cabin (plus a 10 kg member bonus outside business class), then charges for any excess weight at a domestic or international rate, doubling the rate and adding a surcharge when the excess exceeds 20 kg.
*   `carry_on_ok(weight_kg, items, is_infant)` - checks carry-on eligibility, with a relaxed item limit for infants.
*   `check_in_status(minutes_before, has_baggage, is_international)` - reports whether the check-in counter is `open`, `late` or `closed` based on the applicable cut-off time

## work completed
Coverage was measured with the `coverage` library in `--branch` mode so that both statement and branch coverage were reported for every run

*   **Baseline:** the original test file covered `32%` of statements, with `6` partial branches - all `raise` paths, the international and heavy-excess rate logic, and most of `carry_on_ok` / `check_in_status` were untested
*   **Code coverage test file:** added targeted cases for the unknown-cabin and negative-weight `ValueError` paths, the member bonus, the business-class exemption from that bonus, domestic vs international rates, and the heavy-excess surcharge. This reached **100% line coverage**
*   **Branch coverage test file:** built on the same cases and added the one missing outcome - an infant carrying more than two items in `carry_on_ok`. Together with boundary cases on each check-in cut-off (`>= cutoff`, `>= cutoff - 15`, otherwise), every decision in the module evaluates to both true and false. This reached **100% branch coverage**

## final results
*   **Code coverage:** `airline_baggage.py` - `37/37` statements, `0` missed, **100%**
*   **Branch coverage:** `airline_baggage.py` - `26` branches, `0` partial, **100%**
*   **Tests:** `18 passed` (code coverage run) and `19 passed` (branch coverage run)

## directory structure
*   `airline_baggage.py` - The module under test
*   `CodeCoverageTest_AM267_airline_baggage.py` - Test cases for statement/line coverage
*   `BranchCoverageTest_AM267_airline_baggage.py` - Test cases for branch coverage
*   `code_coverage.png` - Terminal output of the final code coverage report
*   `branch_coverage.png` - Terminal output of the final branch coverage report
*   `test_airline_baggage.py` - Original starter test file (unchanged)

## code coverage analysis & report

**Command:** `coverage run -m pytest CodeCoverageTest_AM267_airline_baggage.py` then `coverage report -m`

**Baseline:** the starter tests gave `32%` statement coverage (23 of 37 statements missed). Untested lines were `6, 8, 11, 15-23, 28, 30, 35-45` - i.e. both `ValueError` raises, the member-bonus branch, the whole rate-selection block (`domestic` / `international`, heavy-excess doubling and the international surcharge), and almost all of `carry_on_ok` and `check_in_status`

**Analysis:** the gaps were not random - every missing line sat behind a decision that the two starter tests never flipped. `test_within_allowance` used a non-member economy bag within allowance, so it skipped the member bonus, both rate paths and both raise paths in one go. Adding one case per uncovered decision (unknown cabin, negative weight, member on premium, member on business, international short excess, domestic heavy excess, international heavy excess) executed every remaining statement

**Result:** `18 passed`; `airline_baggage.py` - `37` statements, `0` missed, **100%** statement coverage. Screenshot: `code_coverage.png`

## branch coverage analysis & report

**Command:** `coverage run --branch -m pytest BranchCoverageTest_AM267_airline_baggage.py` then `coverage report -m`

**Baseline:** `26` branches with `6` partial. Statement coverage does not expose these, because a line can be executed while only one side of its decision is ever taken. The partials were the `False` sides of `cabin not in FREE_ALLOWANCE`, `weight_kg < 0`, `is_member and cabin != "business"`, `excess <= 0`, `excess > 20` and the nested `route == "international"`

**Analysis:** the branch run reuses the code-coverage cases - these already cover both outcomes of every decision in `baggage_fee` and `check_in_status`, including the boundary cases on the check-in cut-off (`>= cutoff` for `open`, `>= cutoff - 15` for `late`, otherwise `closed`, with and without baggage, domestic and international). One outcome was still missing: `carry_on_ok` short-circuits on `is_infant`, so `items <= 2` was only ever exercised as true. `test_carry_on_infant_too_many_items` (infant, 3 items) closes it

**Result:** `19 passed`; `airline_baggage.py` - `26` branches, `0` partial, **100%** branch coverage. Screenshot: `branch_coverage.png`