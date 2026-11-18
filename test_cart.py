import pytest

from cart import apply_coupon, cart_total, round_money, subtotal


def test_subtotal():
    assert subtotal([(2.50, 2), (10, 1)]) == 15


def test_round_money_rounds_halves_up():
    assert round_money(2.675) == 2.68
    assert round_money(1.005) == 1.01


def test_percent_coupon():
    assert apply_coupon(200, {"type": "percent", "value": 10}) == 180


def test_fixed_coupon_never_goes_below_zero():
    assert apply_coupon(3, {"type": "fixed", "value": 5}) == 0


def test_unknown_coupon_type():
    with pytest.raises(ValueError):
        apply_coupon(10, {"type": "bogus", "value": 1})


def test_total_without_coupon():
    assert cart_total([(10, 1)]) == 10.80


def test_total_with_percent_coupon_taxes_discounted_amount():
    assert cart_total([(50, 2)], {"type": "percent", "value": 10}) == 97.20


def test_total_with_fixed_coupon():
    assert cart_total([(20, 1), (5, 2)], {"type": "fixed", "value": 5}) == 27.00


def test_total_with_oversized_coupon_is_zero():
    assert cart_total([(4, 1)], {"type": "fixed", "value": 10}) == 0
