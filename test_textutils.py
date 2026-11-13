from textutils import word_count


def test_single_spaces():
    assert word_count("hello big world") == 3


def test_repeated_spaces_and_newlines():
    assert word_count("hello   big\nworld") == 3


def test_empty_and_blank_text():
    assert word_count("") == 0
    assert word_count("   ") == 0
