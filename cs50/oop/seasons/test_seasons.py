from datetime import date, timedelta
import pytest
from seasons import minutes_passed

def test_minutes_passed_two_years():
    # Calculate exactly 2 years ago dynamically based on today's date
    # (Note: Using 730 days or handling leap years programmatically)
    today = date.today()
    # For a rough 2-year check or exact timedelta:
    # Let's say we test 730 days ago (2 years of 365 days):
    expected_days = 730
    assert minutes_passed(str(today - timedelta(days=expected_days))) == expected_days * 24 * 60

def test_minutes_passed_one_year():
    today = date.today()
    expected_days = 365
    # If today or 365 days ago involves a leap day, you can adjust,
    # but for a standard non-leap year offset:
    assert minutes_passed(str(today - timedelta(days=365))) == 365 * 24 * 60

def test_minutes_passed_invalid():
    with pytest.raises(ValueError):
        minutes_passed("November 12, 2025")
    with pytest.raises(ValueError):
        minutes_passed("2025-13-45")
    with pytest.raises(ValueError):
        minutes_passed("2025-02-42")
    with pytest.raises(ValueError):
        minutes_passed("not-a-date")
    with pytest.raises(ValueError):
        minutes_passed("February 6th, 1998")
