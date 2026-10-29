import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# baggage_fee

def test_within_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_unknown_cabin_raises():
    with pytest.raises(ValueError):
        baggage_fee("first", 10, "domestic", False)


def test_negative_weight_raises():
    with pytest.raises(ValueError):
        baggage_fee("economy", -1, "domestic", False)


def test_member_extra_allowance():
    assert baggage_fee("premium", 40, "domestic", True) == 100


def test_member_business_no_bonus():
    assert baggage_fee("business", 40, "domestic", True) == 0


def test_international_short_excess():
    assert baggage_fee("economy", 20, "international", False) == 225


def test_domestic_heavy_excess():
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_international_heavy_excess():
    assert baggage_fee("economy", 50, "international", False) == 3500


# carry_on_ok

def test_carry_on_ok():
    assert carry_on_ok(5, 1, False) is True


def test_carry_on_overweight():
    assert carry_on_ok(8, 1, False) is False


def test_carry_on_too_many_items():
    assert carry_on_ok(5, 2, False) is False


def test_carry_on_infant_ok():
    assert carry_on_ok(10, 2, True) is True


def test_carry_on_infant_too_many_items():
    # closes the last uncovered branch: infant with > 2 items -> False
    assert carry_on_ok(10, 3, True) is False


# check_in_status

def test_check_in_open_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_check_in_open_without_baggage():
    assert check_in_status(45, False, False) == "open"


def test_check_in_late():
    assert check_in_status(50, True, False) == "late"


def test_check_in_closed():
    assert check_in_status(30, True, False) == "closed"


def test_check_in_international_open():
    assert check_in_status(120, True, True) == "open"


def test_check_in_international_late():
    assert check_in_status(100, False, True) == "late"