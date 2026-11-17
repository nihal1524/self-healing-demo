from rangeutils import clamp


def test_value_inside_the_range_is_unchanged():
    assert clamp(5, 0, 10) == 5


def test_value_below_the_range_is_raised_to_low():
    assert clamp(-3, 0, 10) == 0


def test_value_above_the_range_is_lowered_to_high():
    assert clamp(99, 0, 10) == 10
