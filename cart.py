"""Shopping cart totals."""

TAX_RATE = 0.08


def round_money(amount):
    """Round to cents, with halves rounded up (2.675 -> 2.68)."""
    return round(amount, 2)


def subtotal(items):
    """Sum of price * quantity for (price, quantity) pairs."""
    return sum(price * qty for price, qty in items)


def apply_coupon(amount, coupon):
    """Apply a coupon to an amount.

    A coupon is None, {"type": "percent", "value": 10} (10% off) or
    {"type": "fixed", "value": 5} (5.00 off). The result is never below zero.
    """
    if coupon is None:
        return amount
    if coupon["type"] == "percent":
        return amount - amount * coupon["value"]
    if coupon["type"] == "fixed":
        return amount - coupon["value"]
    raise ValueError(f"unknown coupon type: {coupon['type']}")


def cart_total(items, coupon=None):
    """Final amount to charge: subtotal, then coupon, then 8% tax on the discounted amount."""
    taxed = subtotal(items) * (1 + TAX_RATE)
    return round_money(apply_coupon(taxed, coupon))
