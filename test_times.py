from times import compute_overlap_time, time_range

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
        ("2010-01-12 10:15:00", "2010-01-12 10:20:00"),
        ("2010-01-12 10:21:00", "2010-01-12 10:25:00"),
        ("2010-01-12 10:35:00", "2010-01-12 10:40:00"),
        ("2010-01-12 10:41:00", "2010-01-12 10:45:00")
    ]

    assert compute_overlap_time(large, short) == expected

def test_adjacent_ranges():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")

    expected = []
    assert compute_overlap_time(large, short) == expected