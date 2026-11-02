from times import compute_overlap_time, time_range
import pytest

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    expected = []
    assert compute_overlap_time(large, short) == expected

def test_multiple_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 3, 300)
    short = time_range("2010-01-12 10:15:00", "2010-01-12 10:45:00", 2, 60)

    expected = [
    ("2010-01-12 10:15:00", "2010-01-12 10:16:40"),
    ("2010-01-12 10:21:40", "2010-01-12 10:29:30"),
    ("2010-01-12 10:30:30", "2010-01-12 10:38:20"),
    ("2010-01-12 10:43:20", "2010-01-12 10:45:00")
    ]

    assert compute_overlap_time(large, short) == expected

def test_adjacent_ranges():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")

    expected = []
    assert compute_overlap_time(large, short) == expected

# negative test
def test_backwards_time_range():
    with pytest.raises(ValueError, match="End time cannot be earlier than start time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

# -------------------
        
# parametrize
from times import compute_overlap_time, time_range
import pytest

@pytest.mark.parametrize(
    "time_range_1, time_range_2, expected",
    [
        # general case
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [ ("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00") ]
        ),
        # no overlap
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
            []
        ),
        # multiple intervals
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 3, 300),
            time_range("2010-01-12 10:15:00", "2010-01-12 10:45:00", 2, 60),
            [ ("2010-01-12 10:15:00", "2010-01-12 10:16:40"), ("2010-01-12 10:21:40", "2010-01-12 10:29:30"), ("2010-01-12 10:30:30", "2010-01-12 10:38:20"), ("2010-01-12 10:43:20", "2010-01-12 10:45:00") ]
        ),
        # adjacent range
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"),
            []
        )
    ]
)

def test_compute_overlap_time(time_range_1, time_range_2, expected):
    assert compute_overlap_time(time_range_1, time_range_2) == expected

# -------------------------------