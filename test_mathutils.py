from mathutils import average


def test_average_of_several_numbers():
    assert average([2, 4, 6]) == 4


def test_average_of_a_single_number():
    assert average([10]) == 10
