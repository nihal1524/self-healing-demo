def clamp(value, low, high):
    """Limit value to the inclusive range low..high."""
    return min(low, max(value, high))
