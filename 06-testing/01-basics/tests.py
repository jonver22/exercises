from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((3,6), (1,12))
    assert not overlapping_intervals((6,3), (2,5))
    assert not overlapping_intervals((0,0), (1,0))