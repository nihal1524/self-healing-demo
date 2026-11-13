def test_requirement_that_no_code_change_can_satisfy():
    """Deliberately unfixable: used to check what self-healing does when it cannot find a fix."""
    assert 1 + 1 == 3
