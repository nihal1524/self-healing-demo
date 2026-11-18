"""Shopping cart totals."""

TAX_RATE = 0.08


def round_money(amount):
    """Round to cents, with halves rounded up (2.675 -> 2.68)."""
    from decimal import Decimal, ROUND_HALF_UP

    return float(Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


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
        return max(0, amount - amount * coupon["value"] / 100)
    if coupon["type"] == "fixed":
        return max(0, amount - coupon["value"])
    raise ValueError(f"unknown coupon type: {coupon['type']}")


def cart_total(items, coupon=None):
    """Final amount to charge: subtotal, then coupon, then 8% tax on the discounted amount."""
    discounted = apply_coupon(subtotal(items), coupon)
    return round_money(discounted * (1 + TAX_RATE))
